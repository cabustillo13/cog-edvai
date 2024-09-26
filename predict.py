from cog import BasePredictor, Input, Path
import tempfile

from main import rotar_imagen


class Predictor(BasePredictor):
    """Predicción"""
    def predict(
        self,
        imagen: Path = Input(description="Imagen"),
        angulo: int = Input(description="Ángulo de rotación", default=90),
    ) -> Path:
        """Imagen rotada un cierto ángulo"""
        
        # Set Path
        imagen_path = str(imagen)
        
        # Rotar imagen
        output_image = rotar_imagen(imagen_path, angulo)

        # Guardar imagen temporal
        output_path = Path(tempfile.mkdtemp()) / "output.png"
        output_image.save(str(output_path))
    
        return output_path
