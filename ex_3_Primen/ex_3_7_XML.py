# from xml.etree.ElementTree import XMLParser
#
# class Depths:
#     depth = 0
#     clrs = {'red': 0, 'green': 0, 'blue': 0}
#
#     def start(self, tag, attrib):
#         self.depth += 1
#         self.add_w(attrib)
#
#     def add_w(self, attrib):
#         self.clrs[attrib['color']] += self.depth
#
#     def end(self, tag):
#         self.depth -= 1
#
#     def data(self, data):
#         pass
#
#     def close(self):
#         weights_list = [self.clrs['red'], self.clrs['green'], self.clrs['blue']]
#         return ' '.join(list(map(str, weights_list)))
#
# parser = XMLParser(target=Depths())
# parser.feed(input())
# print(parser.close())