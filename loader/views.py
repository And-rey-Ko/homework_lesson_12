from functions import post_upload
from flask import Blueprint, render_template, request, send_from_directory
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post_form/", methods=["GET", "POST"])
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/post_uploaded/", methods=["POST"])
def page_post_upload():
    content = request.form.get("content")
    pic = request.files.get("picture")
    if not content or not pic:
        return "Данные не получены"
    filename = pic.filename
    file_type = filename.split('.')[-1]
    if file_type not in ['jpeg', 'jpg', 'bmp', 'png']:
        return "Файл не картинка"
    pic.save(f"./uploads/images/{filename}")
    pic_path = f"/uploads/images/{filename}"
    post_upload(content, pic_path)
    return render_template('post_uploaded.html', content=content, pic_path=pic_path)


@loader_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)




