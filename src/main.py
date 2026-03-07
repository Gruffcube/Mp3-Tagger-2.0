from pathlib import Path
import logging as log
import time
import os

from utils import old_log_remover

PROGRAM_START_TIME = time.time()

os.system('cls')

CONTRIBUTERS = {
'Gruffcube': ('Primary app developer', 'Find me on GitHub: https://github.com/Gruffcube'),
'TheDigitalArtist': ('Created the placeholder musical note icon', 'Pixabay: https://pixabay.com/users/thedigitalartist-202249/'),
}

def main():
    pass
    
# ======================================================================


if __name__ == '__main__':
    
    # Logging Setup
    LOGS_PATH =  Path.home() / 'MP3_tagger_2.0_logs'
    Path.mkdir(LOGS_PATH, exist_ok=True)
    LOG_FILE = LOGS_PATH / f'{round(time.time())}.log'
    
    log.basicConfig(
        level=log.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            log.FileHandler(LOG_FILE),
            log.StreamHandler()
        ]
    )
    
    
    # Credits
    print(Path.home())
    log.info('Welcome to MP3 tagger 2.0.\n\n')
    
    for key, value in CONTRIBUTERS.items():
        log.info(f'Contributer: {key} \nRole: {value[0]} \nContact: {value[1]}\n\n')
    
    # Execute main()
    
    try:
        main()
            
    except Exception as err:
        log.exception('An unhandled exception occured.')
    
    old_log_remover.remove_old_logs(PROGRAM_START_TIME, LOGS_PATH)
    
    