from repository import Repository
from curator import Curator
from statistics import Statistics
from exporter import Exporter
from renderer import Renderer

repository = Repository()

artifacts = repository.load()

exhibition = Curator().create(

    artifacts

)

stats = Statistics().build(

    exhibition

)

Renderer().show(

    exhibition,

    stats

)

Exporter().save(

    exhibition

)
