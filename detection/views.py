from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image

from .serializers import ImageUploadSerializer


class ImageProcessAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data.get('image')
            image = Image.open(uploaded_file)
            return Response(
                {'image_size': image.size},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
