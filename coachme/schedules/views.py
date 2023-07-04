from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateResponseMixin

class Schedule(TemplateResponseMixin, View):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('delete', False):
            return self.delete(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, *args, username=None):
        '''Отображание главной страницы'''
        context = {"username": username}
        
        return self.render_to_response(context)
    
    def delete(self, request, *args, **kwargs):
        return self.render_to_response({"username":"delete"})
