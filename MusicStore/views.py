from django.views.generic import TemplateView, ListView, DetailView
import requests


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        api_url = 'http://127.0.0.1:9000/api/simple/'
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            formatted_data = [
                {'title': item['title'], 'deezer_id': item['deezer_id']} for item in api_data]

            context['api_data'] = formatted_data

            print(context)
        else:
            context['error_message'] = 'Error obtaining data from the API'

        return context
