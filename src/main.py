from pathlib import Path
import logging as log



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
    
    log.info('This project was made by Gruffcube.')
    
    # Execute main()
    
    try:
        main()
    
    except Exception as err:
        log.exception('An unhandled exception occured.')