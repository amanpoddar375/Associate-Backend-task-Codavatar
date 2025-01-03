from rest_framework import serializers
from .models import VirtualPhoneNumber


class VirtualPhoneNumberSerializer(serializers.ModelSerializer):
    """
    Serializer for Virtual Phone Number model.

    Handles validation and serialization of virtual phone numbers.
    """

    class Meta:
        model = VirtualPhoneNumber
        fields = ["id", "phone_number", "is_active"]
        read_only_fields = ["id"]

    def validate_phone_number(self, value):
        """
        Validate that the phone number is unique across all virtual numbers.

        Args:
            value (str): Phone number to validate

        Returns:
            str: Validated phone number

        Raises:
            serializers.ValidationError: If phone number already exists
        """
        if VirtualPhoneNumber.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already exists")
        return value
