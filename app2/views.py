from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request, "app2/home.html"
        )
import re
from django.utils.timezone import datetime

# class datetime()
# datetime(year, month, day[,hour[,minute[,second]]])
#

def test(request):
    return HttpResponse('sample text')

def hello_there_old(request, name):
    now = datetime.now()
    formatted_now = now.strftime('%A, %d %B, %Y at %X')

    # filters using regex. to restrict URL args to safe chars only
    # now.strftime("%a, %d %b, %Y at %X")

    match_object

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = 'Cora'

    content = "Bonjour, " + clean_name + "! temps et temps " + formatted_now

    return HttpResponse(content)

    # (pattern: AnyStr@match, string: AnyStr@match, flags: _FlagsType = ...) -> Match[AnyStr@match] | None

def hello_there(request, name):
    return render(
        request,
        'app2/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


# (request: HttpRequest, template_name: str | Sequence[str], context: Mapping[str, Any] | None = ..., content_type: str | None = ..., status: int | None = ..., using: str | None = ...) -> HttpResponse
# Return an HttpResponse whose content is filled with the result of calling django.template.loader.render_to_string() with the passed arguments.
