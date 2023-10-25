import json
from app.models import CKEditorPostImages

class CKEditorPostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_superuser and request.method == 'POST' and '/ckeditor/upload/' in request.path:
            try: 
                db_image_recorder = CKEditorPostImages()
                db_image_recorder.name = json.loads(response.content)['fileName']
                db_image_recorder.save()
            except KeyError:
                pass
        return response