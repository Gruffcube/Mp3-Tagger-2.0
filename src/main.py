from pathlib import Path
import logging as log

CONTRIBUTERS = {
'Gruffcube': ('Primary app developer', 'Find me on GitHub: https://github.com/Gruffcube'),
'TheDigitalArtist': ('Created the placeholder musical note icon', 'Pixabay: https://pixabay.com/users/thedigitalartist-202249/'),
}

def main():
    pass
    
# ======================================================================


if __name__ == '__main__':
    
    # Logging Setup
    
    LOG_FILE = Path.home() / 'MP3_tagger_2.0.log'
    log.basicConfig(
        level=log.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            log.FileHandler(LOG_FILE),
            log.StreamHandler()
        ]
    )
    
    # Credits
    log.info('Welcome to MP3 tagger 2.0.')
    
    for key, value in CONTRIBUTERS.items():
        log.info(f'Contributer: {key} \nRole: {value[0]} \nContact: {value[1]}\n\n')
    
    # Execute main()
    
    try:
        main()
    
    except Exception as err:
        log.exception('An unhandled exception occured.')