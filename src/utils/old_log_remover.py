import logging as log
import os



LOG_DELETION_PERIOD = 3600

# Remove old logs

def remove_old_logs(program_start_time, logs_path):
    
    for log_file in logs_path.iterdir():
        try:
            if log_file.suffix.lower() == '.log':
                
                try:
                    log_date = int(log_file.stem)
                
                except:
                    continue
                
                if log_date + LOG_DELETION_PERIOD < program_start_time:
                    os.unlink(log_file)
                    
                    log.info(f'Removed old log file: {log_file}')
        
        except:
            log.info(f'Could not remove log file: {log_file}')