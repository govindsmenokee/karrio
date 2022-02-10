#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Nov 10 10:01:02 2021 by generateDS.py version 2.40.5.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './ups_lib/pre_notification_web_service_schema.py')
#
# Command line arguments:
#   ./schemas/PreNotificationWebServiceSchema.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/purplship/.venv/purplship/bin/generateDS --no-namespace-defs -o "./ups_lib/pre_notification_web_service_schema.py" ./schemas/PreNotificationWebServiceSchema.xsd
#
# Current working directory (os.getcwd()):
#   ups
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
    
    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': None,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    setattr(settings[n], self[n])
            from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % float(input_data)).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class PreNotificationRequest(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Request=None, Shipment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Request = Request
        self.Request_nsprefix_ = "common"
        self.Shipment = Shipment
        self.Shipment_nsprefix_ = "pn"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreNotificationRequest)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreNotificationRequest.subclass:
            return PreNotificationRequest.subclass(*args_, **kwargs_)
        else:
            return PreNotificationRequest(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Request(self):
        return self.Request
    def set_Request(self, Request):
        self.Request = Request
    def get_Shipment(self):
        return self.Shipment
    def set_Shipment(self, Shipment):
        self.Shipment = Shipment
    def _hasContent(self):
        if (
            self.Request is not None or
            self.Shipment is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreNotificationRequest', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreNotificationRequest')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreNotificationRequest':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreNotificationRequest')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreNotificationRequest', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreNotificationRequest'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreNotificationRequest', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Request is not None:
            namespaceprefix_ = self.Request_nsprefix_ + ':' if (UseCapturedNS_ and self.Request_nsprefix_) else ''
            self.Request.export(outfile, level, namespaceprefix_='common:', namespacedef_='', name_='Request', pretty_print=pretty_print)
        if self.Shipment is not None:
            namespaceprefix_ = self.Shipment_nsprefix_ + ':' if (UseCapturedNS_ and self.Shipment_nsprefix_) else ''
            self.Shipment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Shipment', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Request':
            obj_ = RequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Request = obj_
            obj_.original_tagname_ = 'Request'
        elif nodeName_ == 'Shipment':
            obj_ = ShipmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Shipment = obj_
            obj_.original_tagname_ = 'Shipment'
# end class PreNotificationRequest


class PreNotificationResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Response=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Response = Response
        self.Response_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreNotificationResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreNotificationResponse.subclass:
            return PreNotificationResponse.subclass(*args_, **kwargs_)
        else:
            return PreNotificationResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Response(self):
        return self.Response
    def set_Response(self, Response):
        self.Response = Response
    def _hasContent(self):
        if (
            self.Response is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreNotificationResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreNotificationResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreNotificationResponse':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreNotificationResponse')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreNotificationResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreNotificationResponse'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreNotificationResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Response is not None:
            namespaceprefix_ = self.Response_nsprefix_ + ':' if (UseCapturedNS_ and self.Response_nsprefix_) else ''
            self.Response.export(outfile, level, namespaceprefix_='common:', namespacedef_='', name_='Response', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Response':
            obj_ = ResponseType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Response = obj_
            obj_.original_tagname_ = 'Response'
# end class PreNotificationResponse


class AddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, AddressLine=None, City=None, StateProvinceCode=None, PostalCode=None, CountryCode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if AddressLine is None:
            self.AddressLine = []
        else:
            self.AddressLine = AddressLine
        self.AddressLine_nsprefix_ = None
        self.City = City
        self.City_nsprefix_ = None
        self.StateProvinceCode = StateProvinceCode
        self.StateProvinceCode_nsprefix_ = None
        self.PostalCode = PostalCode
        self.PostalCode_nsprefix_ = None
        self.CountryCode = CountryCode
        self.CountryCode_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AddressType.subclass:
            return AddressType.subclass(*args_, **kwargs_)
        else:
            return AddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AddressLine(self):
        return self.AddressLine
    def set_AddressLine(self, AddressLine):
        self.AddressLine = AddressLine
    def add_AddressLine(self, value):
        self.AddressLine.append(value)
    def insert_AddressLine_at(self, index, value):
        self.AddressLine.insert(index, value)
    def replace_AddressLine_at(self, index, value):
        self.AddressLine[index] = value
    def get_City(self):
        return self.City
    def set_City(self, City):
        self.City = City
    def get_StateProvinceCode(self):
        return self.StateProvinceCode
    def set_StateProvinceCode(self, StateProvinceCode):
        self.StateProvinceCode = StateProvinceCode
    def get_PostalCode(self):
        return self.PostalCode
    def set_PostalCode(self, PostalCode):
        self.PostalCode = PostalCode
    def get_CountryCode(self):
        return self.CountryCode
    def set_CountryCode(self, CountryCode):
        self.CountryCode = CountryCode
    def _hasContent(self):
        if (
            self.AddressLine or
            self.City is not None or
            self.StateProvinceCode is not None or
            self.PostalCode is not None or
            self.CountryCode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AddressLine_ in self.AddressLine:
            namespaceprefix_ = self.AddressLine_nsprefix_ + ':' if (UseCapturedNS_ and self.AddressLine_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAddressLine>%s</%sAddressLine>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(AddressLine_), input_name='AddressLine')), namespaceprefix_ , eol_))
        if self.City is not None:
            namespaceprefix_ = self.City_nsprefix_ + ':' if (UseCapturedNS_ and self.City_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCity>%s</%sCity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.City), input_name='City')), namespaceprefix_ , eol_))
        if self.StateProvinceCode is not None:
            namespaceprefix_ = self.StateProvinceCode_nsprefix_ + ':' if (UseCapturedNS_ and self.StateProvinceCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStateProvinceCode>%s</%sStateProvinceCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StateProvinceCode), input_name='StateProvinceCode')), namespaceprefix_ , eol_))
        if self.PostalCode is not None:
            namespaceprefix_ = self.PostalCode_nsprefix_ + ':' if (UseCapturedNS_ and self.PostalCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPostalCode>%s</%sPostalCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PostalCode), input_name='PostalCode')), namespaceprefix_ , eol_))
        if self.CountryCode is not None:
            namespaceprefix_ = self.CountryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CountryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCountryCode>%s</%sCountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CountryCode), input_name='CountryCode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AddressLine':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AddressLine')
            value_ = self.gds_validate_string(value_, node, 'AddressLine')
            self.AddressLine.append(value_)
            self.AddressLine_nsprefix_ = child_.prefix
        elif nodeName_ == 'City':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'City')
            value_ = self.gds_validate_string(value_, node, 'City')
            self.City = value_
            self.City_nsprefix_ = child_.prefix
        elif nodeName_ == 'StateProvinceCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StateProvinceCode')
            value_ = self.gds_validate_string(value_, node, 'StateProvinceCode')
            self.StateProvinceCode = value_
            self.StateProvinceCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'PostalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PostalCode')
            value_ = self.gds_validate_string(value_, node, 'PostalCode')
            self.PostalCode = value_
            self.PostalCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'CountryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CountryCode')
            value_ = self.gds_validate_string(value_, node, 'CountryCode')
            self.CountryCode = value_
            self.CountryCode_nsprefix_ = child_.prefix
# end class AddressType


class PackageType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, TrackingNumber=None, PackageWeight=None, TransportationMode=None, VoidIndicator=None, PackagePoints=None, ChemicalRecord=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TrackingNumber = TrackingNumber
        self.TrackingNumber_nsprefix_ = None
        self.PackageWeight = PackageWeight
        self.PackageWeight_nsprefix_ = "pn"
        self.TransportationMode = TransportationMode
        self.TransportationMode_nsprefix_ = None
        self.VoidIndicator = VoidIndicator
        self.VoidIndicator_nsprefix_ = None
        self.PackagePoints = PackagePoints
        self.PackagePoints_nsprefix_ = None
        if ChemicalRecord is None:
            self.ChemicalRecord = []
        else:
            self.ChemicalRecord = ChemicalRecord
        self.ChemicalRecord_nsprefix_ = "pn"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PackageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PackageType.subclass:
            return PackageType.subclass(*args_, **kwargs_)
        else:
            return PackageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TrackingNumber(self):
        return self.TrackingNumber
    def set_TrackingNumber(self, TrackingNumber):
        self.TrackingNumber = TrackingNumber
    def get_PackageWeight(self):
        return self.PackageWeight
    def set_PackageWeight(self, PackageWeight):
        self.PackageWeight = PackageWeight
    def get_TransportationMode(self):
        return self.TransportationMode
    def set_TransportationMode(self, TransportationMode):
        self.TransportationMode = TransportationMode
    def get_VoidIndicator(self):
        return self.VoidIndicator
    def set_VoidIndicator(self, VoidIndicator):
        self.VoidIndicator = VoidIndicator
    def get_PackagePoints(self):
        return self.PackagePoints
    def set_PackagePoints(self, PackagePoints):
        self.PackagePoints = PackagePoints
    def get_ChemicalRecord(self):
        return self.ChemicalRecord
    def set_ChemicalRecord(self, ChemicalRecord):
        self.ChemicalRecord = ChemicalRecord
    def add_ChemicalRecord(self, value):
        self.ChemicalRecord.append(value)
    def insert_ChemicalRecord_at(self, index, value):
        self.ChemicalRecord.insert(index, value)
    def replace_ChemicalRecord_at(self, index, value):
        self.ChemicalRecord[index] = value
    def _hasContent(self):
        if (
            self.TrackingNumber is not None or
            self.PackageWeight is not None or
            self.TransportationMode is not None or
            self.VoidIndicator is not None or
            self.PackagePoints is not None or
            self.ChemicalRecord
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PackageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PackageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PackageType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PackageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PackageType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TrackingNumber is not None:
            namespaceprefix_ = self.TrackingNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.TrackingNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTrackingNumber>%s</%sTrackingNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TrackingNumber), input_name='TrackingNumber')), namespaceprefix_ , eol_))
        if self.PackageWeight is not None:
            namespaceprefix_ = self.PackageWeight_nsprefix_ + ':' if (UseCapturedNS_ and self.PackageWeight_nsprefix_) else ''
            self.PackageWeight.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PackageWeight', pretty_print=pretty_print)
        if self.TransportationMode is not None:
            namespaceprefix_ = self.TransportationMode_nsprefix_ + ':' if (UseCapturedNS_ and self.TransportationMode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransportationMode>%s</%sTransportationMode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransportationMode), input_name='TransportationMode')), namespaceprefix_ , eol_))
        if self.VoidIndicator is not None:
            namespaceprefix_ = self.VoidIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.VoidIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sVoidIndicator>%s</%sVoidIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.VoidIndicator), input_name='VoidIndicator')), namespaceprefix_ , eol_))
        if self.PackagePoints is not None:
            namespaceprefix_ = self.PackagePoints_nsprefix_ + ':' if (UseCapturedNS_ and self.PackagePoints_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPackagePoints>%s</%sPackagePoints>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PackagePoints), input_name='PackagePoints')), namespaceprefix_ , eol_))
        for ChemicalRecord_ in self.ChemicalRecord:
            namespaceprefix_ = self.ChemicalRecord_nsprefix_ + ':' if (UseCapturedNS_ and self.ChemicalRecord_nsprefix_) else ''
            ChemicalRecord_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChemicalRecord', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TrackingNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TrackingNumber')
            value_ = self.gds_validate_string(value_, node, 'TrackingNumber')
            self.TrackingNumber = value_
            self.TrackingNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackageWeight':
            obj_ = PackageWeightType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PackageWeight = obj_
            obj_.original_tagname_ = 'PackageWeight'
        elif nodeName_ == 'TransportationMode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransportationMode')
            value_ = self.gds_validate_string(value_, node, 'TransportationMode')
            self.TransportationMode = value_
            self.TransportationMode_nsprefix_ = child_.prefix
        elif nodeName_ == 'VoidIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'VoidIndicator')
            value_ = self.gds_validate_string(value_, node, 'VoidIndicator')
            self.VoidIndicator = value_
            self.VoidIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackagePoints':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PackagePoints')
            value_ = self.gds_validate_string(value_, node, 'PackagePoints')
            self.PackagePoints = value_
            self.PackagePoints_nsprefix_ = child_.prefix
        elif nodeName_ == 'ChemicalRecord':
            obj_ = ChemicalRecordType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChemicalRecord.append(obj_)
            obj_.original_tagname_ = 'ChemicalRecord'
# end class PackageType


class ChemicalRecordType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ReportableQuantity=None, ClassDivisionNumber=None, SubRiskClass=None, IDNumber=None, PackagingGroupType=None, Quantity=None, UOM=None, PackagingInstructionCode=None, EmergencyPhone=None, EmergencyContact=None, ProperShippingName=None, TechnicalName=None, AdditionalDescription=None, PackagingType=None, HazardLabelRequired=None, PackagingTypeQuantity=None, CommodityRegulatedLevelCode=None, TransportCategory=None, TunnelRestrictionCode=None, QValue=None, OverPackedIndicator=None, AllPackedInOneIndicator=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ReportableQuantity = ReportableQuantity
        self.ReportableQuantity_nsprefix_ = None
        self.ClassDivisionNumber = ClassDivisionNumber
        self.ClassDivisionNumber_nsprefix_ = None
        self.SubRiskClass = SubRiskClass
        self.SubRiskClass_nsprefix_ = None
        self.IDNumber = IDNumber
        self.IDNumber_nsprefix_ = None
        self.PackagingGroupType = PackagingGroupType
        self.PackagingGroupType_nsprefix_ = None
        self.Quantity = Quantity
        self.Quantity_nsprefix_ = None
        self.UOM = UOM
        self.UOM_nsprefix_ = None
        self.PackagingInstructionCode = PackagingInstructionCode
        self.PackagingInstructionCode_nsprefix_ = None
        self.EmergencyPhone = EmergencyPhone
        self.EmergencyPhone_nsprefix_ = None
        self.EmergencyContact = EmergencyContact
        self.EmergencyContact_nsprefix_ = None
        self.ProperShippingName = ProperShippingName
        self.ProperShippingName_nsprefix_ = None
        self.TechnicalName = TechnicalName
        self.TechnicalName_nsprefix_ = None
        self.AdditionalDescription = AdditionalDescription
        self.AdditionalDescription_nsprefix_ = None
        self.PackagingType = PackagingType
        self.PackagingType_nsprefix_ = None
        self.HazardLabelRequired = HazardLabelRequired
        self.HazardLabelRequired_nsprefix_ = None
        self.PackagingTypeQuantity = PackagingTypeQuantity
        self.PackagingTypeQuantity_nsprefix_ = None
        self.CommodityRegulatedLevelCode = CommodityRegulatedLevelCode
        self.CommodityRegulatedLevelCode_nsprefix_ = None
        self.TransportCategory = TransportCategory
        self.TransportCategory_nsprefix_ = None
        self.TunnelRestrictionCode = TunnelRestrictionCode
        self.TunnelRestrictionCode_nsprefix_ = None
        self.QValue = QValue
        self.QValue_nsprefix_ = None
        self.OverPackedIndicator = OverPackedIndicator
        self.OverPackedIndicator_nsprefix_ = None
        self.AllPackedInOneIndicator = AllPackedInOneIndicator
        self.AllPackedInOneIndicator_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChemicalRecordType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChemicalRecordType.subclass:
            return ChemicalRecordType.subclass(*args_, **kwargs_)
        else:
            return ChemicalRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ReportableQuantity(self):
        return self.ReportableQuantity
    def set_ReportableQuantity(self, ReportableQuantity):
        self.ReportableQuantity = ReportableQuantity
    def get_ClassDivisionNumber(self):
        return self.ClassDivisionNumber
    def set_ClassDivisionNumber(self, ClassDivisionNumber):
        self.ClassDivisionNumber = ClassDivisionNumber
    def get_SubRiskClass(self):
        return self.SubRiskClass
    def set_SubRiskClass(self, SubRiskClass):
        self.SubRiskClass = SubRiskClass
    def get_IDNumber(self):
        return self.IDNumber
    def set_IDNumber(self, IDNumber):
        self.IDNumber = IDNumber
    def get_PackagingGroupType(self):
        return self.PackagingGroupType
    def set_PackagingGroupType(self, PackagingGroupType):
        self.PackagingGroupType = PackagingGroupType
    def get_Quantity(self):
        return self.Quantity
    def set_Quantity(self, Quantity):
        self.Quantity = Quantity
    def get_UOM(self):
        return self.UOM
    def set_UOM(self, UOM):
        self.UOM = UOM
    def get_PackagingInstructionCode(self):
        return self.PackagingInstructionCode
    def set_PackagingInstructionCode(self, PackagingInstructionCode):
        self.PackagingInstructionCode = PackagingInstructionCode
    def get_EmergencyPhone(self):
        return self.EmergencyPhone
    def set_EmergencyPhone(self, EmergencyPhone):
        self.EmergencyPhone = EmergencyPhone
    def get_EmergencyContact(self):
        return self.EmergencyContact
    def set_EmergencyContact(self, EmergencyContact):
        self.EmergencyContact = EmergencyContact
    def get_ProperShippingName(self):
        return self.ProperShippingName
    def set_ProperShippingName(self, ProperShippingName):
        self.ProperShippingName = ProperShippingName
    def get_TechnicalName(self):
        return self.TechnicalName
    def set_TechnicalName(self, TechnicalName):
        self.TechnicalName = TechnicalName
    def get_AdditionalDescription(self):
        return self.AdditionalDescription
    def set_AdditionalDescription(self, AdditionalDescription):
        self.AdditionalDescription = AdditionalDescription
    def get_PackagingType(self):
        return self.PackagingType
    def set_PackagingType(self, PackagingType):
        self.PackagingType = PackagingType
    def get_HazardLabelRequired(self):
        return self.HazardLabelRequired
    def set_HazardLabelRequired(self, HazardLabelRequired):
        self.HazardLabelRequired = HazardLabelRequired
    def get_PackagingTypeQuantity(self):
        return self.PackagingTypeQuantity
    def set_PackagingTypeQuantity(self, PackagingTypeQuantity):
        self.PackagingTypeQuantity = PackagingTypeQuantity
    def get_CommodityRegulatedLevelCode(self):
        return self.CommodityRegulatedLevelCode
    def set_CommodityRegulatedLevelCode(self, CommodityRegulatedLevelCode):
        self.CommodityRegulatedLevelCode = CommodityRegulatedLevelCode
    def get_TransportCategory(self):
        return self.TransportCategory
    def set_TransportCategory(self, TransportCategory):
        self.TransportCategory = TransportCategory
    def get_TunnelRestrictionCode(self):
        return self.TunnelRestrictionCode
    def set_TunnelRestrictionCode(self, TunnelRestrictionCode):
        self.TunnelRestrictionCode = TunnelRestrictionCode
    def get_QValue(self):
        return self.QValue
    def set_QValue(self, QValue):
        self.QValue = QValue
    def get_OverPackedIndicator(self):
        return self.OverPackedIndicator
    def set_OverPackedIndicator(self, OverPackedIndicator):
        self.OverPackedIndicator = OverPackedIndicator
    def get_AllPackedInOneIndicator(self):
        return self.AllPackedInOneIndicator
    def set_AllPackedInOneIndicator(self, AllPackedInOneIndicator):
        self.AllPackedInOneIndicator = AllPackedInOneIndicator
    def _hasContent(self):
        if (
            self.ReportableQuantity is not None or
            self.ClassDivisionNumber is not None or
            self.SubRiskClass is not None or
            self.IDNumber is not None or
            self.PackagingGroupType is not None or
            self.Quantity is not None or
            self.UOM is not None or
            self.PackagingInstructionCode is not None or
            self.EmergencyPhone is not None or
            self.EmergencyContact is not None or
            self.ProperShippingName is not None or
            self.TechnicalName is not None or
            self.AdditionalDescription is not None or
            self.PackagingType is not None or
            self.HazardLabelRequired is not None or
            self.PackagingTypeQuantity is not None or
            self.CommodityRegulatedLevelCode is not None or
            self.TransportCategory is not None or
            self.TunnelRestrictionCode is not None or
            self.QValue is not None or
            self.OverPackedIndicator is not None or
            self.AllPackedInOneIndicator is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChemicalRecordType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChemicalRecordType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChemicalRecordType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChemicalRecordType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChemicalRecordType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChemicalRecordType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChemicalRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ReportableQuantity is not None:
            namespaceprefix_ = self.ReportableQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.ReportableQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sReportableQuantity>%s</%sReportableQuantity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ReportableQuantity), input_name='ReportableQuantity')), namespaceprefix_ , eol_))
        if self.ClassDivisionNumber is not None:
            namespaceprefix_ = self.ClassDivisionNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.ClassDivisionNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sClassDivisionNumber>%s</%sClassDivisionNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ClassDivisionNumber), input_name='ClassDivisionNumber')), namespaceprefix_ , eol_))
        if self.SubRiskClass is not None:
            namespaceprefix_ = self.SubRiskClass_nsprefix_ + ':' if (UseCapturedNS_ and self.SubRiskClass_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSubRiskClass>%s</%sSubRiskClass>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SubRiskClass), input_name='SubRiskClass')), namespaceprefix_ , eol_))
        if self.IDNumber is not None:
            namespaceprefix_ = self.IDNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.IDNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIDNumber>%s</%sIDNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IDNumber), input_name='IDNumber')), namespaceprefix_ , eol_))
        if self.PackagingGroupType is not None:
            namespaceprefix_ = self.PackagingGroupType_nsprefix_ + ':' if (UseCapturedNS_ and self.PackagingGroupType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPackagingGroupType>%s</%sPackagingGroupType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PackagingGroupType), input_name='PackagingGroupType')), namespaceprefix_ , eol_))
        if self.Quantity is not None:
            namespaceprefix_ = self.Quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.Quantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQuantity>%s</%sQuantity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Quantity), input_name='Quantity')), namespaceprefix_ , eol_))
        if self.UOM is not None:
            namespaceprefix_ = self.UOM_nsprefix_ + ':' if (UseCapturedNS_ and self.UOM_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUOM>%s</%sUOM>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UOM), input_name='UOM')), namespaceprefix_ , eol_))
        if self.PackagingInstructionCode is not None:
            namespaceprefix_ = self.PackagingInstructionCode_nsprefix_ + ':' if (UseCapturedNS_ and self.PackagingInstructionCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPackagingInstructionCode>%s</%sPackagingInstructionCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PackagingInstructionCode), input_name='PackagingInstructionCode')), namespaceprefix_ , eol_))
        if self.EmergencyPhone is not None:
            namespaceprefix_ = self.EmergencyPhone_nsprefix_ + ':' if (UseCapturedNS_ and self.EmergencyPhone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmergencyPhone>%s</%sEmergencyPhone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmergencyPhone), input_name='EmergencyPhone')), namespaceprefix_ , eol_))
        if self.EmergencyContact is not None:
            namespaceprefix_ = self.EmergencyContact_nsprefix_ + ':' if (UseCapturedNS_ and self.EmergencyContact_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmergencyContact>%s</%sEmergencyContact>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmergencyContact), input_name='EmergencyContact')), namespaceprefix_ , eol_))
        if self.ProperShippingName is not None:
            namespaceprefix_ = self.ProperShippingName_nsprefix_ + ':' if (UseCapturedNS_ and self.ProperShippingName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProperShippingName>%s</%sProperShippingName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ProperShippingName), input_name='ProperShippingName')), namespaceprefix_ , eol_))
        if self.TechnicalName is not None:
            namespaceprefix_ = self.TechnicalName_nsprefix_ + ':' if (UseCapturedNS_ and self.TechnicalName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTechnicalName>%s</%sTechnicalName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TechnicalName), input_name='TechnicalName')), namespaceprefix_ , eol_))
        if self.AdditionalDescription is not None:
            namespaceprefix_ = self.AdditionalDescription_nsprefix_ + ':' if (UseCapturedNS_ and self.AdditionalDescription_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAdditionalDescription>%s</%sAdditionalDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AdditionalDescription), input_name='AdditionalDescription')), namespaceprefix_ , eol_))
        if self.PackagingType is not None:
            namespaceprefix_ = self.PackagingType_nsprefix_ + ':' if (UseCapturedNS_ and self.PackagingType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPackagingType>%s</%sPackagingType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PackagingType), input_name='PackagingType')), namespaceprefix_ , eol_))
        if self.HazardLabelRequired is not None:
            namespaceprefix_ = self.HazardLabelRequired_nsprefix_ + ':' if (UseCapturedNS_ and self.HazardLabelRequired_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sHazardLabelRequired>%s</%sHazardLabelRequired>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.HazardLabelRequired), input_name='HazardLabelRequired')), namespaceprefix_ , eol_))
        if self.PackagingTypeQuantity is not None:
            namespaceprefix_ = self.PackagingTypeQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.PackagingTypeQuantity_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPackagingTypeQuantity>%s</%sPackagingTypeQuantity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PackagingTypeQuantity), input_name='PackagingTypeQuantity')), namespaceprefix_ , eol_))
        if self.CommodityRegulatedLevelCode is not None:
            namespaceprefix_ = self.CommodityRegulatedLevelCode_nsprefix_ + ':' if (UseCapturedNS_ and self.CommodityRegulatedLevelCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCommodityRegulatedLevelCode>%s</%sCommodityRegulatedLevelCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CommodityRegulatedLevelCode), input_name='CommodityRegulatedLevelCode')), namespaceprefix_ , eol_))
        if self.TransportCategory is not None:
            namespaceprefix_ = self.TransportCategory_nsprefix_ + ':' if (UseCapturedNS_ and self.TransportCategory_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransportCategory>%s</%sTransportCategory>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransportCategory), input_name='TransportCategory')), namespaceprefix_ , eol_))
        if self.TunnelRestrictionCode is not None:
            namespaceprefix_ = self.TunnelRestrictionCode_nsprefix_ + ':' if (UseCapturedNS_ and self.TunnelRestrictionCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTunnelRestrictionCode>%s</%sTunnelRestrictionCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TunnelRestrictionCode), input_name='TunnelRestrictionCode')), namespaceprefix_ , eol_))
        if self.QValue is not None:
            namespaceprefix_ = self.QValue_nsprefix_ + ':' if (UseCapturedNS_ and self.QValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQValue>%s</%sQValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.QValue), input_name='QValue')), namespaceprefix_ , eol_))
        if self.OverPackedIndicator is not None:
            namespaceprefix_ = self.OverPackedIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.OverPackedIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOverPackedIndicator>%s</%sOverPackedIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OverPackedIndicator), input_name='OverPackedIndicator')), namespaceprefix_ , eol_))
        if self.AllPackedInOneIndicator is not None:
            namespaceprefix_ = self.AllPackedInOneIndicator_nsprefix_ + ':' if (UseCapturedNS_ and self.AllPackedInOneIndicator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAllPackedInOneIndicator>%s</%sAllPackedInOneIndicator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AllPackedInOneIndicator), input_name='AllPackedInOneIndicator')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ReportableQuantity':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ReportableQuantity')
            value_ = self.gds_validate_string(value_, node, 'ReportableQuantity')
            self.ReportableQuantity = value_
            self.ReportableQuantity_nsprefix_ = child_.prefix
        elif nodeName_ == 'ClassDivisionNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ClassDivisionNumber')
            value_ = self.gds_validate_string(value_, node, 'ClassDivisionNumber')
            self.ClassDivisionNumber = value_
            self.ClassDivisionNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'SubRiskClass':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SubRiskClass')
            value_ = self.gds_validate_string(value_, node, 'SubRiskClass')
            self.SubRiskClass = value_
            self.SubRiskClass_nsprefix_ = child_.prefix
        elif nodeName_ == 'IDNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IDNumber')
            value_ = self.gds_validate_string(value_, node, 'IDNumber')
            self.IDNumber = value_
            self.IDNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackagingGroupType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PackagingGroupType')
            value_ = self.gds_validate_string(value_, node, 'PackagingGroupType')
            self.PackagingGroupType = value_
            self.PackagingGroupType_nsprefix_ = child_.prefix
        elif nodeName_ == 'Quantity':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Quantity')
            value_ = self.gds_validate_string(value_, node, 'Quantity')
            self.Quantity = value_
            self.Quantity_nsprefix_ = child_.prefix
        elif nodeName_ == 'UOM':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'UOM')
            value_ = self.gds_validate_string(value_, node, 'UOM')
            self.UOM = value_
            self.UOM_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackagingInstructionCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PackagingInstructionCode')
            value_ = self.gds_validate_string(value_, node, 'PackagingInstructionCode')
            self.PackagingInstructionCode = value_
            self.PackagingInstructionCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'EmergencyPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmergencyPhone')
            value_ = self.gds_validate_string(value_, node, 'EmergencyPhone')
            self.EmergencyPhone = value_
            self.EmergencyPhone_nsprefix_ = child_.prefix
        elif nodeName_ == 'EmergencyContact':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmergencyContact')
            value_ = self.gds_validate_string(value_, node, 'EmergencyContact')
            self.EmergencyContact = value_
            self.EmergencyContact_nsprefix_ = child_.prefix
        elif nodeName_ == 'ProperShippingName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ProperShippingName')
            value_ = self.gds_validate_string(value_, node, 'ProperShippingName')
            self.ProperShippingName = value_
            self.ProperShippingName_nsprefix_ = child_.prefix
        elif nodeName_ == 'TechnicalName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TechnicalName')
            value_ = self.gds_validate_string(value_, node, 'TechnicalName')
            self.TechnicalName = value_
            self.TechnicalName_nsprefix_ = child_.prefix
        elif nodeName_ == 'AdditionalDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AdditionalDescription')
            value_ = self.gds_validate_string(value_, node, 'AdditionalDescription')
            self.AdditionalDescription = value_
            self.AdditionalDescription_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackagingType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PackagingType')
            value_ = self.gds_validate_string(value_, node, 'PackagingType')
            self.PackagingType = value_
            self.PackagingType_nsprefix_ = child_.prefix
        elif nodeName_ == 'HazardLabelRequired':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'HazardLabelRequired')
            value_ = self.gds_validate_string(value_, node, 'HazardLabelRequired')
            self.HazardLabelRequired = value_
            self.HazardLabelRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'PackagingTypeQuantity':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PackagingTypeQuantity')
            value_ = self.gds_validate_string(value_, node, 'PackagingTypeQuantity')
            self.PackagingTypeQuantity = value_
            self.PackagingTypeQuantity_nsprefix_ = child_.prefix
        elif nodeName_ == 'CommodityRegulatedLevelCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CommodityRegulatedLevelCode')
            value_ = self.gds_validate_string(value_, node, 'CommodityRegulatedLevelCode')
            self.CommodityRegulatedLevelCode = value_
            self.CommodityRegulatedLevelCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransportCategory':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransportCategory')
            value_ = self.gds_validate_string(value_, node, 'TransportCategory')
            self.TransportCategory = value_
            self.TransportCategory_nsprefix_ = child_.prefix
        elif nodeName_ == 'TunnelRestrictionCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TunnelRestrictionCode')
            value_ = self.gds_validate_string(value_, node, 'TunnelRestrictionCode')
            self.TunnelRestrictionCode = value_
            self.TunnelRestrictionCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'QValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'QValue')
            value_ = self.gds_validate_string(value_, node, 'QValue')
            self.QValue = value_
            self.QValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'OverPackedIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OverPackedIndicator')
            value_ = self.gds_validate_string(value_, node, 'OverPackedIndicator')
            self.OverPackedIndicator = value_
            self.OverPackedIndicator_nsprefix_ = child_.prefix
        elif nodeName_ == 'AllPackedInOneIndicator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AllPackedInOneIndicator')
            value_ = self.gds_validate_string(value_, node, 'AllPackedInOneIndicator')
            self.AllPackedInOneIndicator = value_
            self.AllPackedInOneIndicator_nsprefix_ = child_.prefix
# end class ChemicalRecordType


class PackageWeightType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, UnitOfMeasurement=None, Weight=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.UnitOfMeasurement = UnitOfMeasurement
        self.UnitOfMeasurement_nsprefix_ = None
        self.Weight = Weight
        self.Weight_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PackageWeightType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PackageWeightType.subclass:
            return PackageWeightType.subclass(*args_, **kwargs_)
        else:
            return PackageWeightType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UnitOfMeasurement(self):
        return self.UnitOfMeasurement
    def set_UnitOfMeasurement(self, UnitOfMeasurement):
        self.UnitOfMeasurement = UnitOfMeasurement
    def get_Weight(self):
        return self.Weight
    def set_Weight(self, Weight):
        self.Weight = Weight
    def _hasContent(self):
        if (
            self.UnitOfMeasurement is not None or
            self.Weight is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageWeightType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PackageWeightType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PackageWeightType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PackageWeightType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PackageWeightType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PackageWeightType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PackageWeightType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UnitOfMeasurement is not None:
            namespaceprefix_ = self.UnitOfMeasurement_nsprefix_ + ':' if (UseCapturedNS_ and self.UnitOfMeasurement_nsprefix_) else ''
            self.UnitOfMeasurement.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnitOfMeasurement', pretty_print=pretty_print)
        if self.Weight is not None:
            namespaceprefix_ = self.Weight_nsprefix_ + ':' if (UseCapturedNS_ and self.Weight_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sWeight>%s</%sWeight>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Weight), input_name='Weight')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UnitOfMeasurement':
            obj_ = CodeDescriptionType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnitOfMeasurement = obj_
            obj_.original_tagname_ = 'UnitOfMeasurement'
        elif nodeName_ == 'Weight':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Weight')
            value_ = self.gds_validate_string(value_, node, 'Weight')
            self.Weight = value_
            self.Weight_nsprefix_ = child_.prefix
# end class PackageWeightType


class CodeDescriptionType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CodeDescriptionType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CodeDescriptionType1.subclass:
            return CodeDescriptionType1.subclass(*args_, **kwargs_)
        else:
            return CodeDescriptionType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CodeDescriptionType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CodeDescriptionType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CodeDescriptionType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CodeDescriptionType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CodeDescriptionType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CodeDescriptionType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CodeDescriptionType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
# end class CodeDescriptionType1


class ShipmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ShipperNumber=None, ShipmentIdentificationNumber=None, ShipFromAddress=None, ShipToAddress=None, PickupDate=None, Service=None, RegulationSet=None, Package=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ShipperNumber = ShipperNumber
        self.ShipperNumber_nsprefix_ = None
        self.ShipmentIdentificationNumber = ShipmentIdentificationNumber
        self.ShipmentIdentificationNumber_nsprefix_ = None
        self.ShipFromAddress = ShipFromAddress
        self.ShipFromAddress_nsprefix_ = "pn"
        self.ShipToAddress = ShipToAddress
        self.ShipToAddress_nsprefix_ = "pn"
        self.PickupDate = PickupDate
        self.PickupDate_nsprefix_ = None
        self.Service = Service
        self.Service_nsprefix_ = None
        self.RegulationSet = RegulationSet
        self.RegulationSet_nsprefix_ = None
        if Package is None:
            self.Package = []
        else:
            self.Package = Package
        self.Package_nsprefix_ = "pn"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ShipmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ShipmentType.subclass:
            return ShipmentType.subclass(*args_, **kwargs_)
        else:
            return ShipmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ShipperNumber(self):
        return self.ShipperNumber
    def set_ShipperNumber(self, ShipperNumber):
        self.ShipperNumber = ShipperNumber
    def get_ShipmentIdentificationNumber(self):
        return self.ShipmentIdentificationNumber
    def set_ShipmentIdentificationNumber(self, ShipmentIdentificationNumber):
        self.ShipmentIdentificationNumber = ShipmentIdentificationNumber
    def get_ShipFromAddress(self):
        return self.ShipFromAddress
    def set_ShipFromAddress(self, ShipFromAddress):
        self.ShipFromAddress = ShipFromAddress
    def get_ShipToAddress(self):
        return self.ShipToAddress
    def set_ShipToAddress(self, ShipToAddress):
        self.ShipToAddress = ShipToAddress
    def get_PickupDate(self):
        return self.PickupDate
    def set_PickupDate(self, PickupDate):
        self.PickupDate = PickupDate
    def get_Service(self):
        return self.Service
    def set_Service(self, Service):
        self.Service = Service
    def get_RegulationSet(self):
        return self.RegulationSet
    def set_RegulationSet(self, RegulationSet):
        self.RegulationSet = RegulationSet
    def get_Package(self):
        return self.Package
    def set_Package(self, Package):
        self.Package = Package
    def add_Package(self, value):
        self.Package.append(value)
    def insert_Package_at(self, index, value):
        self.Package.insert(index, value)
    def replace_Package_at(self, index, value):
        self.Package[index] = value
    def _hasContent(self):
        if (
            self.ShipperNumber is not None or
            self.ShipmentIdentificationNumber is not None or
            self.ShipFromAddress is not None or
            self.ShipToAddress is not None or
            self.PickupDate is not None or
            self.Service is not None or
            self.RegulationSet is not None or
            self.Package
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ShipmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ShipmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ShipmentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ShipmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ShipmentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ShipmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ShipperNumber is not None:
            namespaceprefix_ = self.ShipperNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipperNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sShipperNumber>%s</%sShipperNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ShipperNumber), input_name='ShipperNumber')), namespaceprefix_ , eol_))
        if self.ShipmentIdentificationNumber is not None:
            namespaceprefix_ = self.ShipmentIdentificationNumber_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipmentIdentificationNumber_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sShipmentIdentificationNumber>%s</%sShipmentIdentificationNumber>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ShipmentIdentificationNumber), input_name='ShipmentIdentificationNumber')), namespaceprefix_ , eol_))
        if self.ShipFromAddress is not None:
            namespaceprefix_ = self.ShipFromAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipFromAddress_nsprefix_) else ''
            self.ShipFromAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipFromAddress', pretty_print=pretty_print)
        if self.ShipToAddress is not None:
            namespaceprefix_ = self.ShipToAddress_nsprefix_ + ':' if (UseCapturedNS_ and self.ShipToAddress_nsprefix_) else ''
            self.ShipToAddress.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ShipToAddress', pretty_print=pretty_print)
        if self.PickupDate is not None:
            namespaceprefix_ = self.PickupDate_nsprefix_ + ':' if (UseCapturedNS_ and self.PickupDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPickupDate>%s</%sPickupDate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PickupDate), input_name='PickupDate')), namespaceprefix_ , eol_))
        if self.Service is not None:
            namespaceprefix_ = self.Service_nsprefix_ + ':' if (UseCapturedNS_ and self.Service_nsprefix_) else ''
            self.Service.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Service', pretty_print=pretty_print)
        if self.RegulationSet is not None:
            namespaceprefix_ = self.RegulationSet_nsprefix_ + ':' if (UseCapturedNS_ and self.RegulationSet_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRegulationSet>%s</%sRegulationSet>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RegulationSet), input_name='RegulationSet')), namespaceprefix_ , eol_))
        for Package_ in self.Package:
            namespaceprefix_ = self.Package_nsprefix_ + ':' if (UseCapturedNS_ and self.Package_nsprefix_) else ''
            Package_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Package', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ShipperNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ShipperNumber')
            value_ = self.gds_validate_string(value_, node, 'ShipperNumber')
            self.ShipperNumber = value_
            self.ShipperNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'ShipmentIdentificationNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ShipmentIdentificationNumber')
            value_ = self.gds_validate_string(value_, node, 'ShipmentIdentificationNumber')
            self.ShipmentIdentificationNumber = value_
            self.ShipmentIdentificationNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'ShipFromAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipFromAddress = obj_
            obj_.original_tagname_ = 'ShipFromAddress'
        elif nodeName_ == 'ShipToAddress':
            obj_ = AddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ShipToAddress = obj_
            obj_.original_tagname_ = 'ShipToAddress'
        elif nodeName_ == 'PickupDate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PickupDate')
            value_ = self.gds_validate_string(value_, node, 'PickupDate')
            self.PickupDate = value_
            self.PickupDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'Service':
            obj_ = CodeDescriptionType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Service = obj_
            obj_.original_tagname_ = 'Service'
        elif nodeName_ == 'RegulationSet':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RegulationSet')
            value_ = self.gds_validate_string(value_, node, 'RegulationSet')
            self.RegulationSet = value_
            self.RegulationSet_nsprefix_ = child_.prefix
        elif nodeName_ == 'Package':
            obj_ = PackageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Package.append(obj_)
            obj_.original_tagname_ = 'Package'
# end class ShipmentType


class ClientInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Property=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
        self.Property_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ClientInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ClientInformationType.subclass:
            return ClientInformationType.subclass(*args_, **kwargs_)
        else:
            return ClientInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Property(self):
        return self.Property
    def set_Property(self, Property):
        self.Property = Property
    def add_Property(self, value):
        self.Property.append(value)
    def insert_Property_at(self, index, value):
        self.Property.insert(index, value)
    def replace_Property_at(self, index, value):
        self.Property[index] = value
    def _hasContent(self):
        if (
            self.Property
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ClientInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ClientInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ClientInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ClientInformationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ClientInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ClientInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ClientInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            namespaceprefix_ = self.Property_nsprefix_ + ':' if (UseCapturedNS_ and self.Property_nsprefix_) else ''
            Property_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Property', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Property':
            obj_ = PropertyType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Property.append(obj_)
            obj_.original_tagname_ = 'Property'
# end class ClientInformationType


class RequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RequestOption=None, SubVersion=None, TransactionReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if RequestOption is None:
            self.RequestOption = []
        else:
            self.RequestOption = RequestOption
        self.RequestOption_nsprefix_ = None
        self.SubVersion = SubVersion
        self.SubVersion_nsprefix_ = None
        self.TransactionReference = TransactionReference
        self.TransactionReference_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RequestType.subclass:
            return RequestType.subclass(*args_, **kwargs_)
        else:
            return RequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RequestOption(self):
        return self.RequestOption
    def set_RequestOption(self, RequestOption):
        self.RequestOption = RequestOption
    def add_RequestOption(self, value):
        self.RequestOption.append(value)
    def insert_RequestOption_at(self, index, value):
        self.RequestOption.insert(index, value)
    def replace_RequestOption_at(self, index, value):
        self.RequestOption[index] = value
    def get_SubVersion(self):
        return self.SubVersion
    def set_SubVersion(self, SubVersion):
        self.SubVersion = SubVersion
    def get_TransactionReference(self):
        return self.TransactionReference
    def set_TransactionReference(self, TransactionReference):
        self.TransactionReference = TransactionReference
    def _hasContent(self):
        if (
            self.RequestOption or
            self.SubVersion is not None or
            self.TransactionReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='RequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='RequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='RequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for RequestOption_ in self.RequestOption:
            namespaceprefix_ = self.RequestOption_nsprefix_ + ':' if (UseCapturedNS_ and self.RequestOption_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRequestOption>%s</%sRequestOption>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(RequestOption_), input_name='RequestOption')), namespaceprefix_ , eol_))
        if self.SubVersion is not None:
            namespaceprefix_ = self.SubVersion_nsprefix_ + ':' if (UseCapturedNS_ and self.SubVersion_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSubVersion>%s</%sSubVersion>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SubVersion), input_name='SubVersion')), namespaceprefix_ , eol_))
        if self.TransactionReference is not None:
            namespaceprefix_ = self.TransactionReference_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionReference_nsprefix_) else ''
            self.TransactionReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionReference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RequestOption':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RequestOption')
            value_ = self.gds_validate_string(value_, node, 'RequestOption')
            self.RequestOption.append(value_)
            self.RequestOption_nsprefix_ = child_.prefix
        elif nodeName_ == 'SubVersion':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SubVersion')
            value_ = self.gds_validate_string(value_, node, 'SubVersion')
            self.SubVersion = value_
            self.SubVersion_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransactionReference':
            obj_ = TransactionReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionReference = obj_
            obj_.original_tagname_ = 'TransactionReference'
# end class RequestType


class TransactionReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, CustomerContext=None, TransactionIdentifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CustomerContext = CustomerContext
        self.CustomerContext_nsprefix_ = None
        self.TransactionIdentifier = TransactionIdentifier
        self.TransactionIdentifier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransactionReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransactionReferenceType.subclass:
            return TransactionReferenceType.subclass(*args_, **kwargs_)
        else:
            return TransactionReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_CustomerContext(self):
        return self.CustomerContext
    def set_CustomerContext(self, CustomerContext):
        self.CustomerContext = CustomerContext
    def get_TransactionIdentifier(self):
        return self.TransactionIdentifier
    def set_TransactionIdentifier(self, TransactionIdentifier):
        self.TransactionIdentifier = TransactionIdentifier
    def _hasContent(self):
        if (
            self.CustomerContext is not None or
            self.TransactionIdentifier is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='TransactionReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransactionReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransactionReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransactionReferenceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransactionReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='TransactionReferenceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='TransactionReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CustomerContext is not None:
            namespaceprefix_ = self.CustomerContext_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomerContext_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCustomerContext>%s</%sCustomerContext>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CustomerContext), input_name='CustomerContext')), namespaceprefix_ , eol_))
        if self.TransactionIdentifier is not None:
            namespaceprefix_ = self.TransactionIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionIdentifier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTransactionIdentifier>%s</%sTransactionIdentifier>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TransactionIdentifier), input_name='TransactionIdentifier')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CustomerContext':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CustomerContext')
            value_ = self.gds_validate_string(value_, node, 'CustomerContext')
            self.CustomerContext = value_
            self.CustomerContext_nsprefix_ = child_.prefix
        elif nodeName_ == 'TransactionIdentifier':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TransactionIdentifier')
            value_ = self.gds_validate_string(value_, node, 'TransactionIdentifier')
            self.TransactionIdentifier = value_
            self.TransactionIdentifier_nsprefix_ = child_.prefix
# end class TransactionReferenceType


class ResponseType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ResponseStatus=None, Alert=None, AlertDetail=None, TransactionReference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ResponseStatus = ResponseStatus
        self.ResponseStatus_nsprefix_ = "common"
        if Alert is None:
            self.Alert = []
        else:
            self.Alert = Alert
        self.Alert_nsprefix_ = "common"
        if AlertDetail is None:
            self.AlertDetail = []
        else:
            self.AlertDetail = AlertDetail
        self.AlertDetail_nsprefix_ = "common"
        self.TransactionReference = TransactionReference
        self.TransactionReference_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResponseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResponseType.subclass:
            return ResponseType.subclass(*args_, **kwargs_)
        else:
            return ResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ResponseStatus(self):
        return self.ResponseStatus
    def set_ResponseStatus(self, ResponseStatus):
        self.ResponseStatus = ResponseStatus
    def get_Alert(self):
        return self.Alert
    def set_Alert(self, Alert):
        self.Alert = Alert
    def add_Alert(self, value):
        self.Alert.append(value)
    def insert_Alert_at(self, index, value):
        self.Alert.insert(index, value)
    def replace_Alert_at(self, index, value):
        self.Alert[index] = value
    def get_AlertDetail(self):
        return self.AlertDetail
    def set_AlertDetail(self, AlertDetail):
        self.AlertDetail = AlertDetail
    def add_AlertDetail(self, value):
        self.AlertDetail.append(value)
    def insert_AlertDetail_at(self, index, value):
        self.AlertDetail.insert(index, value)
    def replace_AlertDetail_at(self, index, value):
        self.AlertDetail[index] = value
    def get_TransactionReference(self):
        return self.TransactionReference
    def set_TransactionReference(self, TransactionReference):
        self.TransactionReference = TransactionReference
    def _hasContent(self):
        if (
            self.ResponseStatus is not None or
            self.Alert or
            self.AlertDetail or
            self.TransactionReference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ResponseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResponseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResponseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResponseType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResponseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ResponseType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ResponseStatus is not None:
            namespaceprefix_ = self.ResponseStatus_nsprefix_ + ':' if (UseCapturedNS_ and self.ResponseStatus_nsprefix_) else ''
            self.ResponseStatus.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ResponseStatus', pretty_print=pretty_print)
        for Alert_ in self.Alert:
            namespaceprefix_ = self.Alert_nsprefix_ + ':' if (UseCapturedNS_ and self.Alert_nsprefix_) else ''
            Alert_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alert', pretty_print=pretty_print)
        for AlertDetail_ in self.AlertDetail:
            namespaceprefix_ = self.AlertDetail_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertDetail_nsprefix_) else ''
            AlertDetail_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlertDetail', pretty_print=pretty_print)
        if self.TransactionReference is not None:
            namespaceprefix_ = self.TransactionReference_nsprefix_ + ':' if (UseCapturedNS_ and self.TransactionReference_nsprefix_) else ''
            self.TransactionReference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TransactionReference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ResponseStatus':
            obj_ = CodeDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ResponseStatus = obj_
            obj_.original_tagname_ = 'ResponseStatus'
        elif nodeName_ == 'Alert':
            obj_ = CodeDescriptionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alert.append(obj_)
            obj_.original_tagname_ = 'Alert'
        elif nodeName_ == 'AlertDetail':
            obj_ = DetailType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlertDetail.append(obj_)
            obj_.original_tagname_ = 'AlertDetail'
        elif nodeName_ == 'TransactionReference':
            obj_ = TransactionReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TransactionReference = obj_
            obj_.original_tagname_ = 'TransactionReference'
# end class ResponseType


class CodeDescriptionType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CodeDescriptionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CodeDescriptionType.subclass:
            return CodeDescriptionType.subclass(*args_, **kwargs_)
        else:
            return CodeDescriptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='CodeDescriptionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CodeDescriptionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CodeDescriptionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CodeDescriptionType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CodeDescriptionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='CodeDescriptionType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='CodeDescriptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
# end class CodeDescriptionType


class DetailType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Description=None, ElementLevelInformation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
        self.ElementLevelInformation = ElementLevelInformation
        self.ElementLevelInformation_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DetailType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DetailType.subclass:
            return DetailType.subclass(*args_, **kwargs_)
        else:
            return DetailType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Description(self):
        return self.Description
    def set_Description(self, Description):
        self.Description = Description
    def get_ElementLevelInformation(self):
        return self.ElementLevelInformation
    def set_ElementLevelInformation(self, ElementLevelInformation):
        self.ElementLevelInformation = ElementLevelInformation
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Description is not None or
            self.ElementLevelInformation is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='DetailType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DetailType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DetailType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DetailType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DetailType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='DetailType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='DetailType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Description is not None:
            namespaceprefix_ = self.Description_nsprefix_ + ':' if (UseCapturedNS_ and self.Description_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescription>%s</%sDescription>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Description), input_name='Description')), namespaceprefix_ , eol_))
        if self.ElementLevelInformation is not None:
            namespaceprefix_ = self.ElementLevelInformation_nsprefix_ + ':' if (UseCapturedNS_ and self.ElementLevelInformation_nsprefix_) else ''
            self.ElementLevelInformation.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElementLevelInformation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Description')
            value_ = self.gds_validate_string(value_, node, 'Description')
            self.Description = value_
            self.Description_nsprefix_ = child_.prefix
        elif nodeName_ == 'ElementLevelInformation':
            obj_ = ElementLevelInformationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElementLevelInformation = obj_
            obj_.original_tagname_ = 'ElementLevelInformation'
# end class DetailType


class ElementLevelInformationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Level=None, ElementIdentifier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Level = Level
        self.Level_nsprefix_ = None
        if ElementIdentifier is None:
            self.ElementIdentifier = []
        else:
            self.ElementIdentifier = ElementIdentifier
        self.ElementIdentifier_nsprefix_ = "common"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElementLevelInformationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElementLevelInformationType.subclass:
            return ElementLevelInformationType.subclass(*args_, **kwargs_)
        else:
            return ElementLevelInformationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Level(self):
        return self.Level
    def set_Level(self, Level):
        self.Level = Level
    def get_ElementIdentifier(self):
        return self.ElementIdentifier
    def set_ElementIdentifier(self, ElementIdentifier):
        self.ElementIdentifier = ElementIdentifier
    def add_ElementIdentifier(self, value):
        self.ElementIdentifier.append(value)
    def insert_ElementIdentifier_at(self, index, value):
        self.ElementIdentifier.insert(index, value)
    def replace_ElementIdentifier_at(self, index, value):
        self.ElementIdentifier[index] = value
    def _hasContent(self):
        if (
            self.Level is not None or
            self.ElementIdentifier
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementLevelInformationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElementLevelInformationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElementLevelInformationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElementLevelInformationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElementLevelInformationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ElementLevelInformationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementLevelInformationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Level is not None:
            namespaceprefix_ = self.Level_nsprefix_ + ':' if (UseCapturedNS_ and self.Level_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLevel>%s</%sLevel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Level), input_name='Level')), namespaceprefix_ , eol_))
        for ElementIdentifier_ in self.ElementIdentifier:
            namespaceprefix_ = self.ElementIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.ElementIdentifier_nsprefix_) else ''
            ElementIdentifier_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ElementIdentifier', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Level':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Level')
            value_ = self.gds_validate_string(value_, node, 'Level')
            self.Level = value_
            self.Level_nsprefix_ = child_.prefix
        elif nodeName_ == 'ElementIdentifier':
            obj_ = ElementIdentifierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ElementIdentifier.append(obj_)
            obj_.original_tagname_ = 'ElementIdentifier'
# end class ElementLevelInformationType


class ElementIdentifierType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Code=None, Value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Code = Code
        self.Code_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ElementIdentifierType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ElementIdentifierType.subclass:
            return ElementIdentifierType.subclass(*args_, **kwargs_)
        else:
            return ElementIdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Code(self):
        return self.Code
    def set_Code(self, Code):
        self.Code = Code
    def get_Value(self):
        return self.Value
    def set_Value(self, Value):
        self.Value = Value
    def _hasContent(self):
        if (
            self.Code is not None or
            self.Value is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementIdentifierType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ElementIdentifierType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ElementIdentifierType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ElementIdentifierType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ElementIdentifierType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='common:', name_='ElementIdentifierType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='common:', namespacedef_='', name_='ElementIdentifierType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Code is not None:
            namespaceprefix_ = self.Code_nsprefix_ + ':' if (UseCapturedNS_ and self.Code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCode>%s</%sCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Code), input_name='Code')), namespaceprefix_ , eol_))
        if self.Value is not None:
            namespaceprefix_ = self.Value_nsprefix_ + ':' if (UseCapturedNS_ and self.Value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Value), input_name='Value')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Code')
            value_ = self.gds_validate_string(value_, node, 'Code')
            self.Code = value_
            self.Code_nsprefix_ = child_.prefix
        elif nodeName_ == 'Value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Value')
            value_ = self.gds_validate_string(value_, node, 'Value')
            self.Value = value_
            self.Value_nsprefix_ = child_.prefix
# end class ElementIdentifierType


class PropertyType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, Key=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Key = _cast(None, Key)
        self.Key_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PropertyType.subclass:
            return PropertyType.subclass(*args_, **kwargs_)
        else:
            return PropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Key(self):
        return self.Key
    def set_Key(self, Key):
        self.Key = Key
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def _hasContent(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PropertyType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PropertyType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PropertyType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PropertyType')
        if self._hasContent():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PropertyType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PropertyType'):
        if self.Key is not None and 'Key' not in already_processed:
            already_processed.add('Key')
            outfile.write(' Key=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Key), input_name='Key')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PropertyType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Key', node)
        if value is not None and 'Key' not in already_processed:
            already_processed.add('Key')
            self.Key = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PropertyType


GDSClassesMapping = {
    'ClientInformation': ClientInformationType,
    'Request': RequestType,
    'Response': ResponseType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PreNotificationRequest'
        rootClass = PreNotificationRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PreNotificationRequest'
        rootClass = PreNotificationRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PreNotificationRequest'
        rootClass = PreNotificationRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:pn="http://www.ups.com/XMLSchema/XOLTWS/PreNotification/v1.0"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PreNotificationRequest'
        rootClass = PreNotificationRequest
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from pre_notification_web_service_schema import *\n\n')
        sys.stdout.write('import pre_notification_web_service_schema as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
    "{http://www.ups.com/XMLSchema/XOLTWS/PreNotification/v1.0}CodeDescriptionType": "CodeDescriptionType1",
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.ups.com/XMLSchema/XOLTWS/Common/v1.0': [('ClientInformationType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('RequestType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('TransactionReferenceType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ResponseType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('CodeDescriptionType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('DetailType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ElementLevelInformationType',
                                                      './schemas/common.xsd',
                                                      'CT'),
                                                     ('ElementIdentifierType',
                                                      './schemas/common.xsd',
                                                      'CT')],
 'http://www.ups.com/XMLSchema/XOLTWS/PreNotification/v1.0': [('AddressType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT'),
                                                              ('PackageType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT'),
                                                              ('ChemicalRecordType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT'),
                                                              ('PackageWeightType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT'),
                                                              ('CodeDescriptionType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT'),
                                                              ('ShipmentType',
                                                               './schemas/PreNotificationWebServiceSchema.xsd',
                                                               'CT')]}

__all__ = [
    "AddressType",
    "ChemicalRecordType",
    "ClientInformationType",
    "CodeDescriptionType",
    "CodeDescriptionType1",
    "DetailType",
    "ElementIdentifierType",
    "ElementLevelInformationType",
    "PackageType",
    "PackageWeightType",
    "PreNotificationRequest",
    "PreNotificationResponse",
    "PropertyType",
    "RequestType",
    "ResponseType",
    "ShipmentType",
    "TransactionReferenceType"
]