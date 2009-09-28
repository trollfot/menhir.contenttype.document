# -*- coding: utf-8 -*-

import grok
import zope.schema
import dolmen.content as content
import dolmen.forms.crud as crud
import megrok.z3cform.base as z3cform

from html2text import html2text
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.index.text.interfaces import ISearchableText
from dolmen.widget.tinymce.widget import TinyMCEWidgetFactory


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


class RichDocumentCustomize(crud.FieldsCustomizer):
    grok.adapts(Document, z3cform.IGrokForm, Interface)
    
    def __call__(self, fields):
        fields['body'].widgetFactory = TinyMCEWidgetFactory
        return fields
