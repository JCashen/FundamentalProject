import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Locations, Activities

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        SECRET_KEY='TEST_SECRET_KEY',
        DEBUG=True)
        return app

    def setUp(self):
        db.create_all()
        location = Locations(wall_name='The big one', county='Cheshire', town='Chester', postcode='CH1 4HX')
        activity1 = Activities(wall_id =1, activity_name ='Rock Climbing', additional_equiptment =True)
        db.session.add(location)
        db.session.add(activity1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def text_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code,200)

    def test_add_get(self):
        response = self.client.get(url_for('add'))  
        self.assertEqual(response.status_code,200)

    def test_add1_get(self):
        response = self.client.get(url_for('add1', idnum=1))  
        self.assertEqual(response.status_code,200)   

    def test_updateloc_get(self):
        response = self.client.get(url_for("updateloc", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_updateact_get(self):
        response = self.client.get(url_for("updateact", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_viewactivity_get(self):
        response = self.client.get(url_for("viewactivity", idnum=1))
        self.assertEqual(response.status_code,200)

    def test_deleteloc_get(self):
        response = self.client.get(url_for("deleteloc", idnum=1))
        self.assertEqual(response.status_code,302)

    def test_deleteact_get(self):
        response = self.client.get(url_for("deleteact", idnum=1))
        self.assertEqual(response.status_code,302)    