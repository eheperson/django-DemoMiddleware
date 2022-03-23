
class DemoMiddleware:
    """
        Django middleware class has two required methods : 
            __init__
            __call__

        Three optional methods that execute at different points of the view request/tesponse life-cycle
    
        
        Django Middleware Hooks :::::::
            - Called During Request : 
                - process_request(request)
                - process_view(request, view_func, view_args, view_kwargs)
            - Called During Response:
                - process_exception(request, excception)
                    -only if the view raised an exception
                -process_template_response(request, response)
                    - only for template responses
                - process_response(request, response)
    """
    def __init__(self, get_response):
        # one time nfiguration and initialization
        self.get_response = get_response

        # some custom work here
        self.num_requests = 0
        self.num_exceptions = 0
        self.contet_response = {
            "msg": {
                "hi":"hello from world!",
                "bye": "bye..."
            }
        }

    def __call__(self, request):
        """
            code to be executed for each request before 
            the view (and later middleware) are called
        """

        # Some custom work here
        print(" ")
        print(" ")
        print("-----------Those are from DemoMiddleware----------")
        self.num_requests += 1
        print(" ")
        print(" ")
        print("- - - __call__() function - Begin - - -")
        print(f'Exception Count : {self.num_requests}')
        print("enivicivokki middleware called")
        print("hi from __call__(), request is : ", request)
        print("- - - __call__() function - End   - - -")
        print(" ")


        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
            Called just fore django calls the view.
            Returns None or HttpResponse

            Provides access to the view before the request hits the view
        """
        print(" ")
        print("- - - process_view() function - Begin - - -")
        print(f'view name: {view_func.__name__}')
        print("- - - process_view() function - End   - - -")
        print(" ")

    def process_exception(self, request, exception):
        """
            Called for the responsef exception is raised by view
            Returns None or HttpResponse

            Provides a way to capture exceptions from the view
            this function is the part of the response cycle
        """
        # to list all django exceptions
        # from django.core import exceptions
        # ls = list(dir(exceptions))
        # for i in ls:
        #     print(i)
        self.num_exceptions += 1
        print(" ")
        print("- - - process_exception() function - Begin - - -")
        print("hi from process_exception(), exception is : ", exception)
        print("hi from process_exception(), request is : ", request)
        print(f'Exception Count : {self.num_exceptions}')
        print("- - - process_exception() function - End   - - -")
        print(" ")

    def process_template_response(self, request, response):
        """
            request : HttpRequest Object
            response : HttpResponse Object

            returns templateresponse

            This function usefull when we want to change template or context
        """
        response.context_data["new_data"] = self.contet_response

        print(" ")
        print("- - - process_template_response() function - Begin - - -")
        print("hi from process_template_response(), request is : ", request)
        print("hi from process_template_response(), response is : ", response)
        print("- - - process_template_response() function - End - - -")
        print(" ")
        return response