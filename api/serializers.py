from rest_framework import serializers
from .models import Carrera, Usuario, TiposFormatos, Formato, ServicioSocial

class DocumentSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    carrera = serializers.CharField(max_length=100)
    numero_control = serializers.CharField(max_length=20)
    dependencia = serializers.CharField(max_length=100)
    nombre_programa = serializers.CharField(max_length=100)
    titular = serializers.CharField(max_length=100)
    cargo = serializers.CharField(max_length=100)
    atencion_nombre = serializers.CharField(max_length=100)
    atencion_cargo = serializers.CharField(max_length=100)
    



class CarreraSerializer(serializers.ModelSerializer):
    nombre_carrera_display = serializers.SerializerMethodField()

    class Meta:
        model = Carrera
        fields = ['id', 'nombre_carrera', 'nombre_carrera_display']

    def get_nombre_carrera_display(self, obj):
        return obj.get_nombre_carrera_display()


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'tipo_usuario', 'carrera', 'servicio', 'residencia', 'ingles', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tipo_usuario=validated_data['tipo_usuario'],
            carrera=validated_data.get('carrera'),  # get() para campos opcionales
            servicio=validated_data.get('servicio', False),
            residencia=validated_data.get('residencia', False),
            ingles=validated_data.get('ingles', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class TiposFormatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposFormatos
        fields = '__all__'


class FormatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formato
        fields = '__all__'


class ServicioSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioSocial
        fields = '__all__'

    nombre_programa = serializers.CharField(required=False)
    area = serializers.CharField(required=False)
    dependencia_organizacion = serializers.CharField(required=False)
    titular_organizacion = serializers.CharField(required=False)
    cargo_titular = serializers.CharField(required=False)
    atencion_a_nombre = serializers.CharField(required=False)
    atencion_a_cargo = serializers.CharField(required=False)
