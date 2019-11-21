from webapp import app

def startWebserver():
    ''' This function start a Flask webserver for GlobsitSmartDrone webapp 
    '''
    app.run(port=5000)



if  __name__ == "__main__":
    # Run webserver when this file is called by command line
    startWebserver()