from config import DEFAULT_THEME
from config import ARTIFACTS_PER_EXHIBITION

from generator import Generator

class Curator:

    def create(

        self,

        artifacts

    ):

        generator = Generator()

        return {

            "title":

                generator.title(),

            "theme":

                DEFAULT_THEME,

            "items":

                generator.artifacts(

                    artifacts,

                    ARTIFACTS_PER_EXHIBITION

                )

        }
