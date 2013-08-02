"""
RichardHawkins.org (My Website)
Copyright (C) 2013 Richard Hawkins

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from flask import Flask, Response, url_for, render_template
import os


app = Flask(__name__, static_url_path='', static_folder='./static')


def id_to_name(id_, keep_hyphens=False):
    """
    Converts an ID to a friendly name, stripping out thumbnail/data prefixes,
    any .jpg extension, and optionally converting the hyphens to spaces.

    @type  keep_hyphens: boolean
    @param keep_hyphens: If False, strips all hyphens out of the name and
        converts them to spaces.

    @rtype:  string
    @return: The ID converted to a friendly name.
    """
    name = id_

    if name.lower().startswith('d_') or name.lower().startswith('t_'):
        name = name.split('_', 1)[1]

    if name.lower().endswith('.jpg'):
        name = name.rsplit('.', 1)[0]

    if not keep_hyphens:
        name = name.replace('-', ' ')

    return name


def get_galleries():
    """
    Parses the galleries directory and returns information for each gallery
    found.

    @rtype:  list of dictionaries
    @return: Information for each gallery found.
    """
    galleries = []

    gallery_dir = '{0}/static/images/gallery/'.format(
        os.path.realpath(__file__).rsplit('/', 1)[0])

    dirname, dirnames, filenames = next(os.walk(gallery_dir))

    for dirname in dirnames:
        gallery_id = dirname

        thumbnail = 'images/gallery-default-thumbnail.jpg'
        if 't_{0}.jpg'.format(gallery_id) in filenames:
            thumbnail = 'images/gallery/t_{0}.jpg'.format(gallery_id)

        galleries.append({
            'href': url_for('page_gallery_display', gallery_id=gallery_id),
            'thumbnail': url_for('static', filename=thumbnail),
            'name': id_to_name(dirname)})

    return galleries


def get_photos(gallery_id):
    """
    Parses the gallery provide and returns information for each photo found.

    @type:  string
    @param: Gallery ID to retrieve photo information for.

    @rtype:  list of dictionaries
    @return: Information for each photo found.
    """
    photos = []

    photo_dir = '{0}/static/images/gallery/{1}/'.format(
        os.path.realpath(__file__).rsplit('/', 1)[0], gallery_id)

    dirname, dirnames, filenames = next(os.walk(photo_dir))

    for filename in filenames:
        if filename.lower().startswith('d_'):
            photo_id = id_to_name(filename, keep_hyphens=True)
            thumbnail = 'images/gallery/{0}/d_{1}.jpg'.format(
                gallery_id, photo_id)

            if 't_{0}.jpg'.format(photo_id) in filenames:
                thumbnail = 'images/gallery/{0}/t_{1}.jpg'.format(
                    gallery_id, photo_id)

            photos.append({
                'href': url_for(
                    'page_gallery_display_photo', gallery_id=gallery_id,
                    photo_id=photo_id),
                'thumbnail': url_for('static', filename=thumbnail),
                'name': id_to_name(filename)})

    return photos


@app.route('/404error.html')
def page_not_found():
    return render_template('404error.html')


@app.route('/')
def page_root():
    return render_template('root.html')


@app.route('/gallery/')
def page_gallery():
    galleries = get_galleries()
    return render_template('gallery.html', galleries=galleries)


@app.route('/gallery/<gallery_id>/')
def page_gallery_display(gallery_id):
    gallery_name = id_to_name(gallery_id)
    photos = get_photos(gallery_id)
    return render_template(
        'gallery_display.html', gallery_name=gallery_name, photos=photos)


@app.route('/gallery/<gallery_id>/<photo_id>/')
def page_gallery_display_photo(gallery_id, photo_id):
    gallery_name = id_to_name(gallery_id)
    photo_name = id_to_name(photo_id)
    photo_file = 'images/gallery/{0}/d_{1}.jpg'.format(gallery_id, photo_id)
    return render_template(
        'gallery_display_photo.html', gallery_name=gallery_name,
        photo_name=photo_name, photo_file=photo_file)


@app.route('/credits/')
def page_credits():
    return render_template('credits.html')
