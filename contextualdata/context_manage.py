from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)


class ContextManager(object):

    def __init__(self, view_object, view_name, data_object, model_filter,
                 data_filter, data_name, *args, **kwargs):
        self.view_object = view_object
        self.view_name = view_name
        self.data_object = data_object
        self.model_filter = model_filter
        self.data_filter = data_filter
        self.data_name = data_name

    # TODO: Update class to be able to grab and create context_data using DRY
    #       methodology. The method has self not defined issues when being
    #       called from the view class
    def create_context_object(self, *args, **kwargs):
        view = self.view_object
        data_object = self.data_object
        model_filter = self.model_filter
        data_filter = self.data_filter
        view_name = self.view_name

        def get_context_data(view, **kwargs):
            context = super(view_name, view).get_context_data(**kwargs)
            data_name = data_object.objects.filter(model_filter=data_filter)
            context[str(self.data_name)] = data_name
            return context
