# -*- coding: utf-8 -*-

import grok
import zope.schema
import dolmen.content as content
import dolmen.forms.crud as crud
import megrok.z3cform.base as z3cform

from html2text import html2text
from dolmen.app.layout import IDisplayView
from dolmen.widget.tinymce import TINYMCE_INPUT, TINYMCE_DISPLAY
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.index.text.interfaces import ISearchableText


_ = MessageFactory('dolmen')


class IDocument(content.IBaseContent):
    """Defines de document type.
    """
    body = zope.schema.Text(
        title = _(u"Text"),
        required = True,
        )


class Document(content.Content):
    content.name(_("Document"))
    content.schema(IDocument)
    

class SearchableTextDocument(grok.Adapter):
     grok.implements(ISearchableText)

     def getSearchableText(self):
         return (self.context.title, html2text(self.context.body))


class EditRichDocument(crud.FieldsCustomizer):
    grok.adapts(Document, Interface, Interface)

    def __call__(self, fields):
        fields['body'].mode = TINYMCE_INPUT
        return fields


class DiplayRichDocument(crud.FieldsCustomizer):
    grok.adapts(Document, IDisplayView, Interface)

    def __call__(self, fields):
        fields['body'].mode = TINYMCE_DISPLAY
        return fields
