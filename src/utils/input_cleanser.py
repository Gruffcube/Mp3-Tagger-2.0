from pathlib import Path



SUPPORTED_IMAGE_FORMATS = {'.jpg', '.jpeg', '.png'} # NOTE: PNG support has not yet been integrated



def verify_album_cover_exists(path):
    """
    Input a path. Notifies the user if the path is a valid album cover.
    """
    
    
    if not path:
        raise ValueError('No path has been specified.')
    
    path = Path(path)
    
    try:
        if path.is_file:
            
            if path.suffix.lower() in SUPPORTED_IMAGE_FORMATS:
                return path # SUCCESS!!!
                
            else:
                raise ValueError('File format not supported.')
        
        else:
            raise ValueError('File not found. Ensure the path exists and is a file.')
        
    except PermissionError:
        raise PermissionError(f'The user does not have permissions to access this file.')