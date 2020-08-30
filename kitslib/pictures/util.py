from datetime import datetime


class ImageInfo:
    def __init__(self,
            image_id: str,
            thumbnail: str = None,
            large: str = None,
            original: str = None,
            source: str = None,
            rating="s",
            score=0,
            image_copyright=""):
        self.time = datetime.now()
        self.image_id = image_id
        self.thumbnail = thumbnail
        self.large = large
        self.original = original
        self.source = source
        self.rating = rating
        self.score = score
        self.copyright = image_copyright

    def __str__(self):
        return '\n'.join([
            f'id: {self.image_id}',
            f'source: {self.source}',
            f'original: {self.original}',
            '',
            self.copyright
        ])
