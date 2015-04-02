from modeltranslation.translator import TranslationOptions, translator
from languages.models import Language


class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Language, LanguageTranslationOptions)