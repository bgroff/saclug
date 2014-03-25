from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView
from polls.models import Poll, Choice


class PollIndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'polls': Poll.objects.all()
        }


class PollView(TemplateView):
    template_name = 'poll.html'

    def get_context_data(self, **kwargs):
        return {
            'poll': self.poll,
            'error_message': self.error_message if hasattr(self, 'error_message') else None,
        }

    def dispatch(self, request, poll_id, *args, **kwargs):
        self.poll = get_object_or_404(Poll, pk=poll_id)
        return super(PollView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            choice = self.poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            self.error_message = "You didn't select a choice."
            return self.render_to_response(self.get_context_data())

        choice.votes += 1
        choice.save()
        # Always redirect after handling successful POST data. This prevents
        # reposting if the user presses the back button.
        return redirect(reverse('results', args=(self.poll.pk,)))


class ResultsView(TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        return {
            'poll': self.poll,
        }

    def dispatch(self, request, poll_id, *args, **kwargs):
        self.poll = get_object_or_404(Poll, pk=poll_id)
        return super(ResultsView, self).dispatch(request, *args, **kwargs)
