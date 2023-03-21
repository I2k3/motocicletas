from django.test import TestCase

# Create your tests here.
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from motorcycles.schema import schema
from motorcycles.models import Motocicleta

MOTOCICLETAS_QUERY = '''
 {
   motocicletas {
     id
     description
     marca
     modelo
     motor
     consumo_g
     capacidad_g
     cilindraje
     version
     color
     precio 
   }
 }
'''
class  MotocicletaTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.motocicleta1 = mixer.blend(Motocicleta)
        self.motocicleta2 = mixer.blend(Motocicleta)

    def test_motocicletas_query(self):
        response = self.query(
            MOTOCICLETAS_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query motocicleta results ")
        print (content)
        assert len(content['data']['motocicletas']) ==2
