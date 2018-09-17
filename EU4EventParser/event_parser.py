from lexer import Token, Lexer


class Parameter:
    def __init__(self):
        self.name = ""
        self.values = []

    def __repr__(self):
        return "Parameter<"+self.name+","+str(self.values)+">"


class Parser:
    def __init__(self):
        self.events = []
        self.active_event = None
        self.namespace = ""

    def assert_next(self, next_token, should_be):
        if next_token.token_type != should_be:
            raise SyntaxError("Expected {0}, got {1}".format(str(should_be), str(next_token.token_type)))

    def event_file(self, lexer_object):

        if lexer_object.peek_token().token_type == Token.NAMESPACE:
            self.assert_next(lexer_object.get_token(), Token.NAMESPACE)
            self.assert_next(lexer_object.get_token(), Token.EQUALS)
            self.assert_next(lexer_object.peek_token(), Token.TEXT)

            # Get namespace name from TEXT token
            self.namespace = lexer_object.get_token().data

        if lexer_object.peek_token().token_type == Token.TEXT:
            if lexer_object.peek_token().data == "normal_or_historical_nations":
                self.assert_next(lexer_object.get_token(), Token.TEXT)
                self.assert_next(lexer_object.get_token(), Token.EQUALS)
                self.assert_next(lexer_object.get_token(), Token.TEXT)


        self.event_list(lexer_object)

    def event_list(self, lexer_object: Lexer):
        if lexer_object.has_more_tokens():
            self.active_event = Parameter()
            self.events.append(self.active_event)

            self.event(lexer_object)
            #self.parameters(lexer_object, self.active_event.values)
            self.event_list(lexer_object)

    def event(self, lexer_object):
        # Event name

        self.assert_next(lexer_object.peek_token(), Token.TEXT)
        self.active_event.name = lexer_object.get_token().data

        self.assert_next(lexer_object.get_token(), Token.EQUALS)
        self.assert_next(lexer_object.get_token(), Token.OPENBRACE)
        self.parameters(lexer_object, self.active_event.values)

        self.assert_next(lexer_object.get_token(), Token.CLOSEBRACE)

    def parameters(self, lexer_object, parameter_list):
        # TODO: IMPLEMENT THIS PROPERLY
        if not lexer_object.has_more_tokens():
            return

        if lexer_object.peek_token().token_type == Token.TEXT or lexer_object.peek_token().token_type == Token.NUMBER:
            param = Parameter()
            param.name = lexer_object.get_token().data

            if lexer_object.peek_token().token_type != Token.EQUALS:
                return

            lexer_object.get_token()

            parameter_list.append(param)

            if lexer_object.peek_token().token_type == Token.TEXT or lexer_object.peek_token().token_type == Token.NUMBER:
                param.values = lexer_object.get_token().data
                self.parameters(lexer_object, parameter_list)
            else:
                self.assert_next(lexer_object.get_token(), Token.OPENBRACE)
                self.parameters(lexer_object, param.values)
                self.assert_next(lexer_object.get_token(), Token.CLOSEBRACE)
                self.parameters(lexer_object, parameter_list)