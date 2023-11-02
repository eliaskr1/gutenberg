import os


def test_folders_and_files_exist():
    assert "application" in os.listdir(os.curdir)
    assert "__init__.py" in os.listdir(os.curdir + "/application")
    assert "app.py" in os.listdir(os.curdir + "/application")
    assert "func.py" in os.listdir(os.curdir + "/application")
    assert "static" in os.listdir(os.curdir + "/application")
    assert "js" in os.listdir(os.curdir + "/application/static/")
    assert "bootstrap.min.js" in os.listdir(os.curdir + "/application/static/js")
    assert "css" in os.listdir(os.curdir + "/application/static/")
    assert "bootstrap.min.css" in os.listdir(os.curdir + "/application/static/css")
    assert "templates" in os.listdir(os.curdir + "/application")
    assert "layout.html" in os.listdir(os.curdir + "/application/templates/")
    assert "index.html" in os.listdir(os.curdir + "/application/templates/")
    assert "form.html" in os.listdir(os.curdir + "/application/templates/")
    assert "tests" in os.listdir(os.curdir + "/application")
    assert "requirements.txt" in os.listdir(os.curdir)
    assert "header.html" in os.listdir(os.curdir + "/application/templates/")
    assert "table.html" in os.listdir(os.curdir + "/application/templates/")
    assert "error.html" in os.listdir(os.curdir + "/application/templates/")
    assert "footer.html" in os.listdir(os.curdir + "/application/templates/")
    assert "Elias_stjärnor.jpeg" in os.listdir(os.curdir + "/application/static/img")
    assert "img" in os.listdir(os.curdir + "/application/static/")







