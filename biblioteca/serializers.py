from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = ('id','idLibro','idUsuario', 'fecPrestamo', 'fecdevolucion')
    
    def create(self, validated_data):
        """
        Create and return a new `Prestamo` instance, given the validated data.
        """
        return Prestamo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Prestamo` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.idLibro = validated_data.get('idLibro', instance.idLibro)
        instance.idUsuario = validated_data.get('idUsuario', instance.idUsuario)
        instance.fecPrestamo = validated_data.get('fecPrestamo', instance.fecPrestamo)
        instance.fecdevolucion = validated_data.get('fecdevolucion', instance.fecdevolucion)
        instance.save()
        return instance
        

    