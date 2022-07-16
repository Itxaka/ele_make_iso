from django.shortcuts import render, reverse
from django.views import View, generic
from main.models import Jobs
from main.forms import NewJob


class IndexView(generic.View):
    template_name = "index.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class AddNewJobView(generic.CreateView):
    template_name = "form.html"
    model = Jobs
    form_class = NewJob

    def get_success_url(self):
        return reverse("jobs")

    def form_valid(self, form):
        # I guess we create the celery task here and store the uuid
        import uuid
        if form.instance.uuid is None:
            form.instance.uuid = uuid.uuid4()

        return super().form_valid(form)


class ListAllJobs(generic.ListView):
    template_name = "jobs.html"
    queryset = Jobs
