from rest_framework.views import APIView
from .views import CategoryDetailsView, CategoryDestroyView, CategoryUpdateView
from .views import ProductDetailsView, ProductDestroyView, ProductUpdateView

class BaseViewManager(APIView):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)

        return Response(status=405)

class CategoryViewManager(BaseViewManager):
    VIEWS_BY_METHOD = {
        'DELETE': CategoryDestroyView.as_view,
        'GET': CategoryDetailsView.as_view,
        'PUT': CategoryUpdateView.as_view,
        'PATCH': CategoryUpdateView.as_view
    }

class ProductViewManager(BaseViewManager):
    VIEWS_BY_METHOD = {
        'DELETE': ProductDestroyView.as_view,
        'GET': ProductDetailsView.as_view,
        'PUT': ProductUpdateView.as_view,
        'PATCH': ProductUpdateView.as_view
    }
