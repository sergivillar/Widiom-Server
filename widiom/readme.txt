En la librería Modeltranslation hay un fallo que aun no está arreglado. Mientras tanto, se debe cambiar una línea:

En modeltranslation/manager.py:
    Línea 12:
        from django.db.models.fields.related import RelatedField, ForeignObjectRel as RelatedObject


