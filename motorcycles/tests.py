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
   motorcycles {
     id
     description
     marca
     modelo
     motor
     consumog
     capacidadg
     cilindraje
     version
     color
     precio 
   }
 }
'''
CREATE_MOTOCICLETAS_MUTATION = '''
 mutation createMotocicletasMutation( $description: String, $marca: String, $modelo: String, $motor: String, $consumog : Int , $capacidadg: Float, $cilindraje: Int, $version: String, $color : String, $precio : Decimal) {
     createMotocicleta( description: $description, marca: $marca, modelo: $modelo, motor: $motor, consumog: $consumog, capacidadg: $capacidadg, cilindraje: $cilindraje, version: $version, color: $color,precio: $precio) {
      modelo
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
        print(content)
        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        print ("query motocicleta results ")
        print (content)
        assert len(content['data']['motorcycles']) ==2
        
    def test_createMotocicletas_mutation(self):

        response = self.query(
            CREATE_MOTOCICLETAS_MUTATION,
            variables={ 'description': 'Motocicleta 250 blue core, 4tiempos con enfriada de aire', 'marca': 'Yamaha','modelo': 'Fz25', 'motor': 'Blue Core 250 Full Inyection', 'consumog':3,'capacidadg': 14,'cilindraje': 250, 'version':'Fz','color':'Azul tipo Diamante', 'precio':80000.00}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createMotocicleta": {"modelo": "Fz25"}}, content['data']) 
