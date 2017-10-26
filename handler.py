from tornado import web
import json

class DoHandler(web.RequestHandler):
    def get(self, *args):
        try:
            # Print all the info from request
            print "***** "+ str(self.request)
            # Get parameter value
            do_type = self.get_argument("type", None, True)

            if do_type == "direct_ping":
                # Write response
                self.write('success')
                return
        except Exception as ex:
            print ex