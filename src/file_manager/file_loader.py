from pathlib import Path
import logging as log



def load_mp3_files(path):
    """
    Input a path as a string or a path.
    Returns all mp3 files in a specified directory. This is returned as a list
    of paths. If an error occurs, a custom exception is raised detailing the issue 
    instead. Does not search subdirectories.
    """

    
    if not path:
        raise ValueError('No path specified.')
    
    path = Path(path)
    
    try:
        if path.is_dir():
            
            found_mp3s = []
            
            for file in path.iterdir():
                try:
                    if not file.is_file():
                        continue
                    
                    
                    if file.suffix.lower() == '.mp3':

                        found_mp3s.append(file)
                        
                        log.info(f'Sucessfully found file {file}.')
                    
                    else:
                        log.info(f'Could not open {file} due to it not being an mp3 file.')
                    
                    
                except PermissionError:
                    log.warning(f'Could not open {file} due to a permission error.')
                    continue
            
            return found_mp3s
        
        
        else:
            raise ValueError('Path is not a directory.')
    
    except PermissionError:
        raise PermissionError('Access denied. This may be a restricted or system folder.')