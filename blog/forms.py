from django.forms import ModelForm, ClearableFileInput
from .models import Post

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'archivo')
        widgets = {
            'archivo': CustomClearableFileInput
        }
