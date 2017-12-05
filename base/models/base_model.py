import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from permissions.decorators import check_permission

from ..custom_exceptions import MissUseError
from ..utils import get_model_field_names
from .soft_deletion_model import SoftDeletionModel

from django.core.exceptions import Exception


class BaseModel(SoftDeletionModel):
    """
    Base model for this project.

    Contains the base properties and methods for all models.
    """

    uuid = models.UUIDField(
        verbose_name=_('Unique Identifier'),
        help_text=_('Unique Identifier.'),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
        help_text=_('Keep this record active or not.')
    )
    is_archived = models.BooleanField(
        verbose_name=_('Is Archived'),
        default=False,
        help_text=_('Keep this record active or not.')
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Created By'),
        help_text=_('User Who Create This Record'),
        related_name='created_by',
        null=True, blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Updated By'),
        help_text=_('User Who Last Update This Record'),
        related_name='updated_by',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        verbose_name=_('DateTime Created'),
        help_text=_('Creation Date.'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('DateTime Updated'),
        help_text=_('Last Update.'),
        auto_now=True,
    )

    def _check_permission(self,
                          user,
                          permission,
                          model):
        """
        Checks the permission of a user in a model
        :param user: who's permission have to be checked
        :param permission: name of the permission like 'add', change
        :param model: which model's permission has to check

        :return: Boolean value
        """
        permission_name = ''
        permission_name = "{permission}_{model}".format(
            permission=permission,
            model=model.to_lower())
        return getattr(user, permission_name)

    def create(self, *args, **kwargs):
        """
        Creates an object and return that
        """
        permission = "add"
        if not created_by:
            raise Exception("'created_by' must be supplied."
        if not self._check_permission(user=created_by,
                                      permission=permission,
                                      model=self.__class__.__name__):
            raise Exception("User doesn't have ADD permission in {model}.".format(
                model=self.__class__.__name__))
        return super(BaseModel, self).create(*args, **kwargs)

    def update(self, *args, **kwargs):
        """
        Updates an object and return number of objects is updated
        """
        permission="change"
        if not updated_by:
            raise Exception("'updated_by' must be supplied.")

        if not self._check_permission(user=updated_by,
                                      permission=permission,
                                      model=self.__class__.__name__):
            raise Exception("User doesn't have CHANGE permission in {model}.".format(
                model=self.__class__.__name__))
        return super(BaseModel, self).update(*args, **kwargs)

    def _created_at(self):
        return self.created_at.date().isoformat()

    def _update_at(self):
        return self.updated_at.date().isoformat()

    created_at=property(_created_at)
    updated_at=property(_update_at)

    class Meta:
        abstract=True
