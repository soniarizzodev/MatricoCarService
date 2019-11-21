import json
import time

from webapp.API.Response import Response

TOTAL_ROWS = 8
DATA_FOLDER = 'data/'


def sync(data):
    response = Response(True)
    
    try:
        # Check data integrity
        rows = 0
        for sector in data['sectors']:
            for row in sector['rows']:
                rows += 1

        if rows == TOTAL_ROWS:     
            
            with open(DATA_FOLDER + "matricocar/backups/" + str(time.time()) + ".json", "w") as fp:
                # Save backup data to json
                json.dump(data, fp)
        
            with open(DATA_FOLDER + "matricocar/plant.json", "w") as fp:
                # Save data to json
                json.dump(data, fp)

        else:
            raise Exception('WRONG DATA FORMAT')

    except Exception as e:
        response.status = False
        response.message = "WRONG DATA FORMAT - {}".format(str(e))


    return response.compose()

