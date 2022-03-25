from django.urls import path
from app2 import views

urlpatterns = [
    path("app2/home", views.home, name='home'),
    path('app2/<name>', views.hello_there, name='hello_there')
]

# (route: str, view: (...) -> HttpResponseBase, kwargs: Dict[str, Any] = ..., name: str = ...) -> URLPattern
# (route: str, view: Sequence[URLResolver | str], kwargs: Dict[str, Any] = ..., name: str = ...) -> URLResolver
# (route: str, view: Sequence[URLResolver | str], kwargs: Dict[str, Any] = ..., name: str = ...) -> URLResolver
