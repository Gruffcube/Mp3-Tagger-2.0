import eyed3
from eyed3.core import Date
import logging as log



class Song:
    '''
    This class contains all of the infomation related to a song as well as
    some relevent functions.
    '''
    def __init__(path):
        self.path = Path(path)
        
        self.title = Path(path).name
        self.index = None # This index starts at 1
        
        self.album_title = None
        self.album_artist = None
        self.album_cover = None # Must be a path to an image file
        
        self.release_year = None
        
        self.genres = []
        
        self.contributing_artists = []
        
        
        
    def write_song_metadata(self, rename=False, album_length=None):
        '''
        Writes all of the song metadata to the file. Renames the file to
        the format "## Song Name" if the argument "rename" is True (False
        by default).
        '''
        audio = eyed3.load(self.path)
        
        if audio.tag is None:
            audio.initTag()
        
        if album_length:
            audio.tag.track_num = (self.index, album_length)
        else:
            audio.tag.track_num = (self.index)
        
        if self.title:
            audio.tag.title = self.title
        
        if self.album_title:
            audio.tag.album = self.album_title
        
        if self.album_artist:
            audio.tag.album_artist = self.album_artist
        
        if self.release_year:
            audio.tag.recording_date = Date(int(self.release_year))
            
        if self.genres:
            audio.tag.genre = "; ".join(self.genres)
            
        if self.contributing_artists:
            audio.tag.artist = "; ".join(self.contributing_artists)
        
        try:
            if self.album_cover:
                with open(self.album_cover, 'rb') as img_file:
                    audio.tag.images.set(
                    3,
                    img_file.read(),
                    'image/jpeg'
                    )
        
        
        except PermissionError:
            log.warning(f'Cannot access image file "{self.album_cover.name}". Reason: PermissionError')
        
        except Exception:
            log.exception(f'Cannot access image file "{self.album_cover.name}". Reason: PermissionError')
        
        
        if rename:
            try:
                new_filename = self.path.parent / f'{self.index:02} {self.title}.mp3'
                
                if new_filename.exists():
                    new_filename.unlink()
                os.rename(self.path, new_filename)
            
            except PermissionError:
                log.warning(f'Cannot rename MP3 file "{self.path.name}". Reason: PermissionError')
        
            except Exception:
                log.exception(f'Cannot rename MP3 file "{self.path.name}". Reason:')
        
        
        
        audio.tag.save()