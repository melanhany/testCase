from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=40)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    explicit_url = models.CharField(max_length=255, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=255, blank=True, null=True, unique=True)    

    def __str__(self) -> str:
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_parent_ids(self):
        if self.parent:
            return self.parent.get_parent_ids() + [self.parent.id]
        else:
            return []