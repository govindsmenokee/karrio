#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jul 14 15:39:45 2021 by generateDS.py version 2.39.2.
# Python 3.8.6 (v3.8.6:db455296be, Sep 23 2020, 13:31:39)  [Clang 6.0 (clang-600.0.57)]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('-o', './canadapost_lib/pickuprequest.py')
#
# Command line arguments:
#   ./schemas/pickuprequest.xsd
#
# Command line:
#   /Users/danielkobina/Workspace/project/karrio-carriers/.venv/karrio-carriers/bin/generateDS --no-namespace-defs -o "./canadapost_lib/pickuprequest.py" ./schemas/pickuprequest.xsd
#
# Current working directory (os.getcwd()):
#   canadapost
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
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


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
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
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
            return ('%.15f' % input_data).rstrip('0')
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
    def to_etree(self, element, mapping_=None, nsmap_=None):
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
    def to_etree_simple(self, mapping_=None, nsmap_=None):
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


class DayOfTheWeekType(str, Enum):
    MON='MON'
    TUE='TUE'
    WED='WED'
    THU='THU'
    FRI='FRI'


class MethodOfPaymentType(str, Enum):
    CREDIT_CARD='CreditCard'
    ACCOUNT='Account'
    SUPPLIER_ACCOUNT='SupplierAccount'


class PickupStatusType(str, Enum):
    ACTIVE='Active'
    NEW='New'
    CANCELLED='Cancelled'
    PENDING='Pending'
    MISSED_PICKUP='Missed Pickup'


class PickupTypeType(str, Enum):
    ON_DEMAND='OnDemand'
    SCHEDULED='Scheduled'


class PickupRequestDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, customer_request_id=None, pickup_type=None, pickup_location=None, contact_info=None, location_details=None, items_characteristics=None, pickup_volume=None, pickup_times=None, payment_info=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer_request_id = customer_request_id
        self.validate_CustomerRequestIDType(self.customer_request_id)
        self.customer_request_id_nsprefix_ = None
        self.pickup_type = pickup_type
        self.validate_PickupTypeType(self.pickup_type)
        self.pickup_type_nsprefix_ = None
        self.pickup_location = pickup_location
        self.pickup_location_nsprefix_ = None
        self.contact_info = contact_info
        self.contact_info_nsprefix_ = None
        self.location_details = location_details
        self.location_details_nsprefix_ = None
        self.items_characteristics = items_characteristics
        self.items_characteristics_nsprefix_ = None
        self.pickup_volume = pickup_volume
        self.validate_PickupVolumeType(self.pickup_volume)
        self.pickup_volume_nsprefix_ = None
        self.pickup_times = pickup_times
        self.pickup_times_nsprefix_ = None
        self.payment_info = payment_info
        self.payment_info_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestDetailsType.subclass:
            return PickupRequestDetailsType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_customer_request_id(self):
        return self.customer_request_id
    def set_customer_request_id(self, customer_request_id):
        self.customer_request_id = customer_request_id
    def get_pickup_type(self):
        return self.pickup_type
    def set_pickup_type(self, pickup_type):
        self.pickup_type = pickup_type
    def get_pickup_location(self):
        return self.pickup_location
    def set_pickup_location(self, pickup_location):
        self.pickup_location = pickup_location
    def get_contact_info(self):
        return self.contact_info
    def set_contact_info(self, contact_info):
        self.contact_info = contact_info
    def get_location_details(self):
        return self.location_details
    def set_location_details(self, location_details):
        self.location_details = location_details
    def get_items_characteristics(self):
        return self.items_characteristics
    def set_items_characteristics(self, items_characteristics):
        self.items_characteristics = items_characteristics
    def get_pickup_volume(self):
        return self.pickup_volume
    def set_pickup_volume(self, pickup_volume):
        self.pickup_volume = pickup_volume
    def get_pickup_times(self):
        return self.pickup_times
    def set_pickup_times(self, pickup_times):
        self.pickup_times = pickup_times
    def get_payment_info(self):
        return self.payment_info
    def set_payment_info(self, payment_info):
        self.payment_info = payment_info
    def validate_CustomerRequestIDType(self, value):
        result = True
        # Validate type CustomerRequestIDType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CustomerRequestIDType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CustomerRequestIDType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PickupTypeType(self, value):
        result = True
        # Validate type PickupTypeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OnDemand', 'Scheduled']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PickupTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_PickupVolumeType(self, value):
        result = True
        # Validate type PickupVolumeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PickupVolumeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PickupVolumeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.customer_request_id is not None or
            self.pickup_type is not None or
            self.pickup_location is not None or
            self.contact_info is not None or
            self.location_details is not None or
            self.items_characteristics is not None or
            self.pickup_volume is not None or
            self.pickup_times is not None or
            self.payment_info is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.customer_request_id is not None:
            namespaceprefix_ = self.customer_request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scustomer-request-id>%s</%scustomer-request-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.customer_request_id), input_name='customer-request-id')), namespaceprefix_ , eol_))
        if self.pickup_type is not None:
            namespaceprefix_ = self.pickup_type_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-type>%s</%spickup-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_type), input_name='pickup-type')), namespaceprefix_ , eol_))
        if self.pickup_location is not None:
            namespaceprefix_ = self.pickup_location_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_location_nsprefix_) else ''
            self.pickup_location.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-location', pretty_print=pretty_print)
        if self.contact_info is not None:
            namespaceprefix_ = self.contact_info_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_info_nsprefix_) else ''
            self.contact_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contact-info', pretty_print=pretty_print)
        if self.location_details is not None:
            namespaceprefix_ = self.location_details_nsprefix_ + ':' if (UseCapturedNS_ and self.location_details_nsprefix_) else ''
            self.location_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location-details', pretty_print=pretty_print)
        if self.items_characteristics is not None:
            namespaceprefix_ = self.items_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.items_characteristics_nsprefix_) else ''
            self.items_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='items-characteristics', pretty_print=pretty_print)
        if self.pickup_volume is not None:
            namespaceprefix_ = self.pickup_volume_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_volume_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-volume>%s</%spickup-volume>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_volume), input_name='pickup-volume')), namespaceprefix_ , eol_))
        if self.pickup_times is not None:
            namespaceprefix_ = self.pickup_times_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_times_nsprefix_) else ''
            self.pickup_times.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-times', pretty_print=pretty_print)
        if self.payment_info is not None:
            namespaceprefix_ = self.payment_info_nsprefix_ + ':' if (UseCapturedNS_ and self.payment_info_nsprefix_) else ''
            self.payment_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='payment-info', pretty_print=pretty_print)
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
        if nodeName_ == 'customer-request-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'customer_request_id')
            value_ = self.gds_validate_string(value_, node, 'customer_request_id')
            self.customer_request_id = value_
            self.customer_request_id_nsprefix_ = child_.prefix
            # validate type CustomerRequestIDType
            self.validate_CustomerRequestIDType(self.customer_request_id)
        elif nodeName_ == 'pickup-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_type')
            value_ = self.gds_validate_string(value_, node, 'pickup_type')
            self.pickup_type = value_
            self.pickup_type_nsprefix_ = child_.prefix
            # validate type PickupTypeType
            self.validate_PickupTypeType(self.pickup_type)
        elif nodeName_ == 'pickup-location':
            obj_ = PickupLocationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_location = obj_
            obj_.original_tagname_ = 'pickup-location'
        elif nodeName_ == 'contact-info':
            obj_ = ContactInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact_info = obj_
            obj_.original_tagname_ = 'contact-info'
        elif nodeName_ == 'location-details':
            obj_ = LocationDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location_details = obj_
            obj_.original_tagname_ = 'location-details'
        elif nodeName_ == 'items-characteristics':
            obj_ = ItemsCharacteristicsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.items_characteristics = obj_
            obj_.original_tagname_ = 'items-characteristics'
        elif nodeName_ == 'pickup-volume':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_volume')
            value_ = self.gds_validate_string(value_, node, 'pickup_volume')
            self.pickup_volume = value_
            self.pickup_volume_nsprefix_ = child_.prefix
            # validate type PickupVolumeType
            self.validate_PickupVolumeType(self.pickup_volume)
        elif nodeName_ == 'pickup-times':
            obj_ = PickupTimesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_times = obj_
            obj_.original_tagname_ = 'pickup-times'
        elif nodeName_ == 'payment-info':
            obj_ = PaymentInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.payment_info = obj_
            obj_.original_tagname_ = 'payment-info'
# end class PickupRequestDetailsType


class PickupRequestUpdateDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, contact_info=None, location_details=None, items_characteristics=None, pickup_volume=None, pickup_times=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.contact_info = contact_info
        self.contact_info_nsprefix_ = None
        self.location_details = location_details
        self.location_details_nsprefix_ = None
        self.items_characteristics = items_characteristics
        self.items_characteristics_nsprefix_ = None
        self.pickup_volume = pickup_volume
        self.validate_PickupVolumeType(self.pickup_volume)
        self.pickup_volume_nsprefix_ = None
        self.pickup_times = pickup_times
        self.pickup_times_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestUpdateDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestUpdateDetailsType.subclass:
            return PickupRequestUpdateDetailsType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestUpdateDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contact_info(self):
        return self.contact_info
    def set_contact_info(self, contact_info):
        self.contact_info = contact_info
    def get_location_details(self):
        return self.location_details
    def set_location_details(self, location_details):
        self.location_details = location_details
    def get_items_characteristics(self):
        return self.items_characteristics
    def set_items_characteristics(self, items_characteristics):
        self.items_characteristics = items_characteristics
    def get_pickup_volume(self):
        return self.pickup_volume
    def set_pickup_volume(self, pickup_volume):
        self.pickup_volume = pickup_volume
    def get_pickup_times(self):
        return self.pickup_times
    def set_pickup_times(self, pickup_times):
        self.pickup_times = pickup_times
    def validate_PickupVolumeType(self, value):
        result = True
        # Validate type PickupVolumeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PickupVolumeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PickupVolumeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.contact_info is not None or
            self.location_details is not None or
            self.items_characteristics is not None or
            self.pickup_volume is not None or
            self.pickup_times is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestUpdateDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestUpdateDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestUpdateDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestUpdateDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestUpdateDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestUpdateDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestUpdateDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.contact_info is not None:
            namespaceprefix_ = self.contact_info_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_info_nsprefix_) else ''
            self.contact_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contact-info', pretty_print=pretty_print)
        if self.location_details is not None:
            namespaceprefix_ = self.location_details_nsprefix_ + ':' if (UseCapturedNS_ and self.location_details_nsprefix_) else ''
            self.location_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location-details', pretty_print=pretty_print)
        if self.items_characteristics is not None:
            namespaceprefix_ = self.items_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.items_characteristics_nsprefix_) else ''
            self.items_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='items-characteristics', pretty_print=pretty_print)
        if self.pickup_volume is not None:
            namespaceprefix_ = self.pickup_volume_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_volume_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-volume>%s</%spickup-volume>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_volume), input_name='pickup-volume')), namespaceprefix_ , eol_))
        if self.pickup_times is not None:
            namespaceprefix_ = self.pickup_times_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_times_nsprefix_) else ''
            self.pickup_times.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-times', pretty_print=pretty_print)
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
        if nodeName_ == 'contact-info':
            obj_ = ContactInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact_info = obj_
            obj_.original_tagname_ = 'contact-info'
        elif nodeName_ == 'location-details':
            obj_ = LocationDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location_details = obj_
            obj_.original_tagname_ = 'location-details'
        elif nodeName_ == 'items-characteristics':
            obj_ = ItemsCharacteristicsUpdateDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.items_characteristics = obj_
            obj_.original_tagname_ = 'items-characteristics'
        elif nodeName_ == 'pickup-volume':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_volume')
            value_ = self.gds_validate_string(value_, node, 'pickup_volume')
            self.pickup_volume = value_
            self.pickup_volume_nsprefix_ = child_.prefix
            # validate type PickupVolumeType
            self.validate_PickupVolumeType(self.pickup_volume)
        elif nodeName_ == 'pickup-times':
            obj_ = PickupTimesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_times = obj_
            obj_.original_tagname_ = 'pickup-times'
# end class PickupRequestUpdateDetailsType


class PickupRequestsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_request=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if pickup_request is None:
            self.pickup_request = []
        else:
            self.pickup_request = pickup_request
        self.pickup_request_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestsType.subclass:
            return PickupRequestsType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_request(self):
        return self.pickup_request
    def set_pickup_request(self, pickup_request):
        self.pickup_request = pickup_request
    def add_pickup_request(self, value):
        self.pickup_request.append(value)
    def insert_pickup_request_at(self, index, value):
        self.pickup_request.insert(index, value)
    def replace_pickup_request_at(self, index, value):
        self.pickup_request[index] = value
    def _hasContent(self):
        if (
            self.pickup_request
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for pickup_request_ in self.pickup_request:
            namespaceprefix_ = self.pickup_request_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_nsprefix_) else ''
            pickup_request_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-request':
            obj_ = PickupRequestType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request.append(obj_)
            obj_.original_tagname_ = 'pickup-request'
# end class PickupRequestsType


class PickupDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, date=None, contract_id=None, pww_flag=None, priority_flag=None, alternate_address_province=None, alternate_address_postal_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            initvalue_ = date
        self.date = initvalue_
        self.date_nsprefix_ = None
        self.contract_id = contract_id
        self.validate_ContractIDType(self.contract_id)
        self.contract_id_nsprefix_ = None
        self.pww_flag = pww_flag
        self.pww_flag_nsprefix_ = None
        self.priority_flag = priority_flag
        self.priority_flag_nsprefix_ = None
        self.alternate_address_province = alternate_address_province
        self.validate_ProvinceType(self.alternate_address_province)
        self.alternate_address_province_nsprefix_ = None
        self.alternate_address_postal_code = alternate_address_postal_code
        self.validate_PostalCodeType(self.alternate_address_postal_code)
        self.alternate_address_postal_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupDetailsType.subclass:
            return PickupDetailsType.subclass(*args_, **kwargs_)
        else:
            return PickupDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def get_contract_id(self):
        return self.contract_id
    def set_contract_id(self, contract_id):
        self.contract_id = contract_id
    def get_pww_flag(self):
        return self.pww_flag
    def set_pww_flag(self, pww_flag):
        self.pww_flag = pww_flag
    def get_priority_flag(self):
        return self.priority_flag
    def set_priority_flag(self, priority_flag):
        self.priority_flag = priority_flag
    def get_alternate_address_province(self):
        return self.alternate_address_province
    def set_alternate_address_province(self, alternate_address_province):
        self.alternate_address_province = alternate_address_province
    def get_alternate_address_postal_code(self):
        return self.alternate_address_postal_code
    def set_alternate_address_postal_code(self, alternate_address_postal_code):
        self.alternate_address_postal_code = alternate_address_postal_code
    def validate_ContractIDType(self, value):
        result = True
        # Validate type ContractIDType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_ContractIDType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ContractIDType_patterns_, ))
                result = False
        return result
    validate_ContractIDType_patterns_ = [['^(\\d{1,10})$']]
    def validate_ProvinceType(self, value):
        result = True
        # Validate type ProvinceType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProvinceType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProvinceType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PostalCodeType(self, value):
        result = True
        # Validate type PostalCodeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PostalCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PostalCodeType_patterns_, ))
                result = False
        return result
    validate_PostalCodeType_patterns_ = [['^([A-Z]\\d[A-Z]\\d[A-Z]\\d)$']]
    def _hasContent(self):
        if (
            self.date is not None or
            self.contract_id is not None or
            self.pww_flag is not None or
            self.priority_flag is not None or
            self.alternate_address_province is not None or
            self.alternate_address_postal_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.date is not None:
            namespaceprefix_ = self.date_nsprefix_ + ':' if (UseCapturedNS_ and self.date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdate>%s</%sdate>%s' % (namespaceprefix_ , self.gds_format_date(self.date, input_name='date'), namespaceprefix_ , eol_))
        if self.contract_id is not None:
            namespaceprefix_ = self.contract_id_nsprefix_ + ':' if (UseCapturedNS_ and self.contract_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontract-id>%s</%scontract-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contract_id), input_name='contract-id')), namespaceprefix_ , eol_))
        if self.pww_flag is not None:
            namespaceprefix_ = self.pww_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.pww_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spww-flag>%s</%spww-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.pww_flag, input_name='pww-flag'), namespaceprefix_ , eol_))
        if self.priority_flag is not None:
            namespaceprefix_ = self.priority_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.priority_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spriority-flag>%s</%spriority-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.priority_flag, input_name='priority-flag'), namespaceprefix_ , eol_))
        if self.alternate_address_province is not None:
            namespaceprefix_ = self.alternate_address_province_nsprefix_ + ':' if (UseCapturedNS_ and self.alternate_address_province_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%salternate-address-province>%s</%salternate-address-province>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.alternate_address_province), input_name='alternate-address-province')), namespaceprefix_ , eol_))
        if self.alternate_address_postal_code is not None:
            namespaceprefix_ = self.alternate_address_postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.alternate_address_postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%salternate-address-postal-code>%s</%salternate-address-postal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.alternate_address_postal_code), input_name='alternate-address-postal-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.date = dval_
            self.date_nsprefix_ = child_.prefix
        elif nodeName_ == 'contract-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contract_id')
            value_ = self.gds_validate_string(value_, node, 'contract_id')
            self.contract_id = value_
            self.contract_id_nsprefix_ = child_.prefix
            # validate type ContractIDType
            self.validate_ContractIDType(self.contract_id)
        elif nodeName_ == 'pww-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'pww_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'pww_flag')
            self.pww_flag = ival_
            self.pww_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'priority-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'priority_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'priority_flag')
            self.priority_flag = ival_
            self.priority_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'alternate-address-province':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'alternate_address_province')
            value_ = self.gds_validate_string(value_, node, 'alternate_address_province')
            self.alternate_address_province = value_
            self.alternate_address_province_nsprefix_ = child_.prefix
            # validate type ProvinceType
            self.validate_ProvinceType(self.alternate_address_province)
        elif nodeName_ == 'alternate-address-postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'alternate_address_postal_code')
            value_ = self.gds_validate_string(value_, node, 'alternate_address_postal_code')
            self.alternate_address_postal_code = value_
            self.alternate_address_postal_code_nsprefix_ = child_.prefix
            # validate type PostalCodeType
            self.validate_PostalCodeType(self.alternate_address_postal_code)
# end class PickupDetailsType


class PickupRequestInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_request_header=None, pickup_request_price=None, links=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pickup_request_header = pickup_request_header
        self.pickup_request_header_nsprefix_ = None
        self.pickup_request_price = pickup_request_price
        self.pickup_request_price_nsprefix_ = None
        self.links = links
        self.links_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestInfoType.subclass:
            return PickupRequestInfoType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_request_header(self):
        return self.pickup_request_header
    def set_pickup_request_header(self, pickup_request_header):
        self.pickup_request_header = pickup_request_header
    def get_pickup_request_price(self):
        return self.pickup_request_price
    def set_pickup_request_price(self, pickup_request_price):
        self.pickup_request_price = pickup_request_price
    def get_links(self):
        return self.links
    def set_links(self, links):
        self.links = links
    def _hasContent(self):
        if (
            self.pickup_request_header is not None or
            self.pickup_request_price is not None or
            self.links is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pickup_request_header is not None:
            namespaceprefix_ = self.pickup_request_header_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_header_nsprefix_) else ''
            self.pickup_request_header.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request-header', pretty_print=pretty_print)
        if self.pickup_request_price is not None:
            namespaceprefix_ = self.pickup_request_price_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_price_nsprefix_) else ''
            self.pickup_request_price.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request-price', pretty_print=pretty_print)
        if self.links is not None:
            namespaceprefix_ = self.links_nsprefix_ + ':' if (UseCapturedNS_ and self.links_nsprefix_) else ''
            self.links.export(outfile, level, namespaceprefix_, namespacedef_='', name_='links', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-request-header':
            obj_ = PickupRequestHeaderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request_header = obj_
            obj_.original_tagname_ = 'pickup-request-header'
        elif nodeName_ == 'pickup-request-price':
            obj_ = PickupRequestPriceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request_price = obj_
            obj_.original_tagname_ = 'pickup-request-price'
        elif nodeName_ == 'links':
            obj_ = linksType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.links = obj_
            obj_.original_tagname_ = 'links'
# end class PickupRequestInfoType


class PickupRequestType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_request_header=None, links=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pickup_request_header = pickup_request_header
        self.pickup_request_header_nsprefix_ = None
        self.links = links
        self.links_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestType.subclass:
            return PickupRequestType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_request_header(self):
        return self.pickup_request_header
    def set_pickup_request_header(self, pickup_request_header):
        self.pickup_request_header = pickup_request_header
    def get_links(self):
        return self.links
    def set_links(self, links):
        self.links = links
    def _hasContent(self):
        if (
            self.pickup_request_header is not None or
            self.links is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pickup_request_header is not None:
            namespaceprefix_ = self.pickup_request_header_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_header_nsprefix_) else ''
            self.pickup_request_header.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request-header', pretty_print=pretty_print)
        if self.links is not None:
            namespaceprefix_ = self.links_nsprefix_ + ':' if (UseCapturedNS_ and self.links_nsprefix_) else ''
            self.links.export(outfile, level, namespaceprefix_, namespacedef_='', name_='links', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-request-header':
            obj_ = PickupRequestHeaderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request_header = obj_
            obj_.original_tagname_ = 'pickup-request-header'
        elif nodeName_ == 'links':
            obj_ = linksType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.links = obj_
            obj_.original_tagname_ = 'links'
# end class PickupRequestType


class PickupRequestDetailedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_request_header=None, pickup_request_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pickup_request_header = pickup_request_header
        self.pickup_request_header_nsprefix_ = None
        self.pickup_request_details = pickup_request_details
        self.pickup_request_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestDetailedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestDetailedInfoType.subclass:
            return PickupRequestDetailedInfoType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestDetailedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_request_header(self):
        return self.pickup_request_header
    def set_pickup_request_header(self, pickup_request_header):
        self.pickup_request_header = pickup_request_header
    def get_pickup_request_details(self):
        return self.pickup_request_details
    def set_pickup_request_details(self, pickup_request_details):
        self.pickup_request_details = pickup_request_details
    def _hasContent(self):
        if (
            self.pickup_request_header is not None or
            self.pickup_request_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestDetailedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestDetailedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestDetailedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestDetailedInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestDetailedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestDetailedInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestDetailedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pickup_request_header is not None:
            namespaceprefix_ = self.pickup_request_header_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_header_nsprefix_) else ''
            self.pickup_request_header.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request-header', pretty_print=pretty_print)
        if self.pickup_request_details is not None:
            namespaceprefix_ = self.pickup_request_details_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_request_details_nsprefix_) else ''
            self.pickup_request_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-request-details', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-request-header':
            obj_ = PickupRequestHeaderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request_header = obj_
            obj_.original_tagname_ = 'pickup-request-header'
        elif nodeName_ == 'pickup-request-details':
            obj_ = PickupRequestResponseDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_request_details = obj_
            obj_.original_tagname_ = 'pickup-request-details'
# end class PickupRequestDetailedInfoType


class PickupRequestResponseDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_location=None, contact_info=None, location_details=None, items_characteristics=None, pickup_volume=None, pickup_times=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pickup_location = pickup_location
        self.pickup_location_nsprefix_ = None
        self.contact_info = contact_info
        self.contact_info_nsprefix_ = None
        self.location_details = location_details
        self.location_details_nsprefix_ = None
        self.items_characteristics = items_characteristics
        self.items_characteristics_nsprefix_ = None
        self.pickup_volume = pickup_volume
        self.validate_PickupVolumeType(self.pickup_volume)
        self.pickup_volume_nsprefix_ = None
        self.pickup_times = pickup_times
        self.pickup_times_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestResponseDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestResponseDetailsType.subclass:
            return PickupRequestResponseDetailsType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestResponseDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_location(self):
        return self.pickup_location
    def set_pickup_location(self, pickup_location):
        self.pickup_location = pickup_location
    def get_contact_info(self):
        return self.contact_info
    def set_contact_info(self, contact_info):
        self.contact_info = contact_info
    def get_location_details(self):
        return self.location_details
    def set_location_details(self, location_details):
        self.location_details = location_details
    def get_items_characteristics(self):
        return self.items_characteristics
    def set_items_characteristics(self, items_characteristics):
        self.items_characteristics = items_characteristics
    def get_pickup_volume(self):
        return self.pickup_volume
    def set_pickup_volume(self, pickup_volume):
        self.pickup_volume = pickup_volume
    def get_pickup_times(self):
        return self.pickup_times
    def set_pickup_times(self, pickup_times):
        self.pickup_times = pickup_times
    def validate_PickupVolumeType(self, value):
        result = True
        # Validate type PickupVolumeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PickupVolumeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PickupVolumeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.pickup_location is not None or
            self.contact_info is not None or
            self.location_details is not None or
            self.items_characteristics is not None or
            self.pickup_volume is not None or
            self.pickup_times is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestResponseDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestResponseDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestResponseDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestResponseDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestResponseDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestResponseDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestResponseDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pickup_location is not None:
            namespaceprefix_ = self.pickup_location_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_location_nsprefix_) else ''
            self.pickup_location.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-location', pretty_print=pretty_print)
        if self.contact_info is not None:
            namespaceprefix_ = self.contact_info_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_info_nsprefix_) else ''
            self.contact_info.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contact-info', pretty_print=pretty_print)
        if self.location_details is not None:
            namespaceprefix_ = self.location_details_nsprefix_ + ':' if (UseCapturedNS_ and self.location_details_nsprefix_) else ''
            self.location_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location-details', pretty_print=pretty_print)
        if self.items_characteristics is not None:
            namespaceprefix_ = self.items_characteristics_nsprefix_ + ':' if (UseCapturedNS_ and self.items_characteristics_nsprefix_) else ''
            self.items_characteristics.export(outfile, level, namespaceprefix_, namespacedef_='', name_='items-characteristics', pretty_print=pretty_print)
        if self.pickup_volume is not None:
            namespaceprefix_ = self.pickup_volume_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_volume_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-volume>%s</%spickup-volume>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_volume), input_name='pickup-volume')), namespaceprefix_ , eol_))
        if self.pickup_times is not None:
            namespaceprefix_ = self.pickup_times_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_times_nsprefix_) else ''
            self.pickup_times.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-times', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-location':
            obj_ = PickupLocationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_location = obj_
            obj_.original_tagname_ = 'pickup-location'
        elif nodeName_ == 'contact-info':
            obj_ = ContactInfoResponseDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact_info = obj_
            obj_.original_tagname_ = 'contact-info'
        elif nodeName_ == 'location-details':
            obj_ = LocationDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location_details = obj_
            obj_.original_tagname_ = 'location-details'
        elif nodeName_ == 'items-characteristics':
            obj_ = ItemsCharacteristicsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.items_characteristics = obj_
            obj_.original_tagname_ = 'items-characteristics'
        elif nodeName_ == 'pickup-volume':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_volume')
            value_ = self.gds_validate_string(value_, node, 'pickup_volume')
            self.pickup_volume = value_
            self.pickup_volume_nsprefix_ = child_.prefix
            # validate type PickupVolumeType
            self.validate_PickupVolumeType(self.pickup_volume)
        elif nodeName_ == 'pickup-times':
            obj_ = PickupTimesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_times = obj_
            obj_.original_tagname_ = 'pickup-times'
# end class PickupRequestResponseDetailsType


class HoldPickupsInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, effective_date=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(effective_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(effective_date, '%Y-%m-%d').date()
        else:
            initvalue_ = effective_date
        self.effective_date = initvalue_
        self.effective_date_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, HoldPickupsInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if HoldPickupsInfoType.subclass:
            return HoldPickupsInfoType.subclass(*args_, **kwargs_)
        else:
            return HoldPickupsInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_effective_date(self):
        return self.effective_date
    def set_effective_date(self, effective_date):
        self.effective_date = effective_date
    def _hasContent(self):
        if (
            self.effective_date is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='HoldPickupsInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('HoldPickupsInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'HoldPickupsInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='HoldPickupsInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='HoldPickupsInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='HoldPickupsInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='HoldPickupsInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.effective_date is not None:
            namespaceprefix_ = self.effective_date_nsprefix_ + ':' if (UseCapturedNS_ and self.effective_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seffective-date>%s</%seffective-date>%s' % (namespaceprefix_ , self.gds_format_date(self.effective_date, input_name='effective-date'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'effective-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.effective_date = dval_
            self.effective_date_nsprefix_ = child_.prefix
# end class HoldPickupsInfoType


class ResumePickupsInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, effective_date=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(effective_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(effective_date, '%Y-%m-%d').date()
        else:
            initvalue_ = effective_date
        self.effective_date = initvalue_
        self.effective_date_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ResumePickupsInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ResumePickupsInfoType.subclass:
            return ResumePickupsInfoType.subclass(*args_, **kwargs_)
        else:
            return ResumePickupsInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_effective_date(self):
        return self.effective_date
    def set_effective_date(self, effective_date):
        self.effective_date = effective_date
    def _hasContent(self):
        if (
            self.effective_date is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResumePickupsInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ResumePickupsInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ResumePickupsInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ResumePickupsInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ResumePickupsInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ResumePickupsInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ResumePickupsInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.effective_date is not None:
            namespaceprefix_ = self.effective_date_nsprefix_ + ':' if (UseCapturedNS_ and self.effective_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seffective-date>%s</%seffective-date>%s' % (namespaceprefix_ , self.gds_format_date(self.effective_date, input_name='effective-date'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'effective-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.effective_date = dval_
            self.effective_date_nsprefix_ = child_.prefix
# end class ResumePickupsInfoType


class PickupLocationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, business_address_flag=None, alternate_address=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.business_address_flag = business_address_flag
        self.business_address_flag_nsprefix_ = None
        self.alternate_address = alternate_address
        self.alternate_address_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupLocationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupLocationType.subclass:
            return PickupLocationType.subclass(*args_, **kwargs_)
        else:
            return PickupLocationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_business_address_flag(self):
        return self.business_address_flag
    def set_business_address_flag(self, business_address_flag):
        self.business_address_flag = business_address_flag
    def get_alternate_address(self):
        return self.alternate_address
    def set_alternate_address(self, alternate_address):
        self.alternate_address = alternate_address
    def _hasContent(self):
        if (
            self.business_address_flag is not None or
            self.alternate_address is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupLocationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupLocationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupLocationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupLocationType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupLocationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupLocationType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupLocationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.business_address_flag is not None:
            namespaceprefix_ = self.business_address_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.business_address_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbusiness-address-flag>%s</%sbusiness-address-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.business_address_flag, input_name='business-address-flag'), namespaceprefix_ , eol_))
        if self.alternate_address is not None:
            namespaceprefix_ = self.alternate_address_nsprefix_ + ':' if (UseCapturedNS_ and self.alternate_address_nsprefix_) else ''
            self.alternate_address.export(outfile, level, namespaceprefix_, namespacedef_='', name_='alternate-address', pretty_print=pretty_print)
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
        if nodeName_ == 'business-address-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'business_address_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'business_address_flag')
            self.business_address_flag = ival_
            self.business_address_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'alternate-address':
            obj_ = AlternateAddressType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.alternate_address = obj_
            obj_.original_tagname_ = 'alternate-address'
# end class PickupLocationType


class AlternateAddressType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, company=None, address_line_1=None, city=None, province=None, postal_code=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.company = company
        self.validate_companyType(self.company)
        self.company_nsprefix_ = None
        self.address_line_1 = address_line_1
        self.validate_address_line_1Type(self.address_line_1)
        self.address_line_1_nsprefix_ = None
        self.city = city
        self.validate_cityType(self.city)
        self.city_nsprefix_ = None
        self.province = province
        self.validate_ProvinceType(self.province)
        self.province_nsprefix_ = None
        self.postal_code = postal_code
        self.validate_PostalCodeType(self.postal_code)
        self.postal_code_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AlternateAddressType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AlternateAddressType.subclass:
            return AlternateAddressType.subclass(*args_, **kwargs_)
        else:
            return AlternateAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_company(self):
        return self.company
    def set_company(self, company):
        self.company = company
    def get_address_line_1(self):
        return self.address_line_1
    def set_address_line_1(self, address_line_1):
        self.address_line_1 = address_line_1
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def get_province(self):
        return self.province
    def set_province(self, province):
        self.province = province
    def get_postal_code(self):
        return self.postal_code
    def set_postal_code(self, postal_code):
        self.postal_code = postal_code
    def validate_companyType(self, value):
        result = True
        # Validate type companyType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on companyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_address_line_1Type(self, value):
        result = True
        # Validate type address-line-1Type, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on address-line-1Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cityType(self, value):
        result = True
        # Validate type cityType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on cityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ProvinceType(self, value):
        result = True
        # Validate type ProvinceType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ProvinceType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ProvinceType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PostalCodeType(self, value):
        result = True
        # Validate type PostalCodeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PostalCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PostalCodeType_patterns_, ))
                result = False
        return result
    validate_PostalCodeType_patterns_ = [['^([A-Z]\\d[A-Z]\\d[A-Z]\\d)$']]
    def _hasContent(self):
        if (
            self.company is not None or
            self.address_line_1 is not None or
            self.city is not None or
            self.province is not None or
            self.postal_code is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AlternateAddressType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AlternateAddressType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AlternateAddressType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AlternateAddressType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AlternateAddressType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AlternateAddressType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AlternateAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.company is not None:
            namespaceprefix_ = self.company_nsprefix_ + ':' if (UseCapturedNS_ and self.company_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scompany>%s</%scompany>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.company), input_name='company')), namespaceprefix_ , eol_))
        if self.address_line_1 is not None:
            namespaceprefix_ = self.address_line_1_nsprefix_ + ':' if (UseCapturedNS_ and self.address_line_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-line-1>%s</%saddress-line-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.address_line_1), input_name='address-line-1')), namespaceprefix_ , eol_))
        if self.city is not None:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.city), input_name='city')), namespaceprefix_ , eol_))
        if self.province is not None:
            namespaceprefix_ = self.province_nsprefix_ + ':' if (UseCapturedNS_ and self.province_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprovince>%s</%sprovince>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.province), input_name='province')), namespaceprefix_ , eol_))
        if self.postal_code is not None:
            namespaceprefix_ = self.postal_code_nsprefix_ + ':' if (UseCapturedNS_ and self.postal_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostal-code>%s</%spostal-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.postal_code), input_name='postal-code')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'company':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'company')
            value_ = self.gds_validate_string(value_, node, 'company')
            self.company = value_
            self.company_nsprefix_ = child_.prefix
            # validate type companyType
            self.validate_companyType(self.company)
        elif nodeName_ == 'address-line-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'address_line_1')
            value_ = self.gds_validate_string(value_, node, 'address_line_1')
            self.address_line_1 = value_
            self.address_line_1_nsprefix_ = child_.prefix
            # validate type address-line-1Type
            self.validate_address_line_1Type(self.address_line_1)
        elif nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city = value_
            self.city_nsprefix_ = child_.prefix
            # validate type cityType
            self.validate_cityType(self.city)
        elif nodeName_ == 'province':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'province')
            value_ = self.gds_validate_string(value_, node, 'province')
            self.province = value_
            self.province_nsprefix_ = child_.prefix
            # validate type ProvinceType
            self.validate_ProvinceType(self.province)
        elif nodeName_ == 'postal-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postal_code')
            value_ = self.gds_validate_string(value_, node, 'postal_code')
            self.postal_code = value_
            self.postal_code_nsprefix_ = child_.prefix
            # validate type PostalCodeType
            self.validate_PostalCodeType(self.postal_code)
# end class AlternateAddressType


class ContactInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, contact_name=None, email=None, contact_phone=None, telephone_ext=None, receive_email_updates_flag=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.contact_name = contact_name
        self.validate_contact_nameType(self.contact_name)
        self.contact_name_nsprefix_ = None
        self.email = email
        self.validate_EmailType(self.email)
        self.email_nsprefix_ = None
        self.contact_phone = contact_phone
        self.validate_PhoneType(self.contact_phone)
        self.contact_phone_nsprefix_ = None
        self.telephone_ext = telephone_ext
        self.validate_PhoneExtentionType(self.telephone_ext)
        self.telephone_ext_nsprefix_ = None
        self.receive_email_updates_flag = receive_email_updates_flag
        self.receive_email_updates_flag_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ContactInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ContactInfoType.subclass:
            return ContactInfoType.subclass(*args_, **kwargs_)
        else:
            return ContactInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contact_name(self):
        return self.contact_name
    def set_contact_name(self, contact_name):
        self.contact_name = contact_name
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_contact_phone(self):
        return self.contact_phone
    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone
    def get_telephone_ext(self):
        return self.telephone_ext
    def set_telephone_ext(self, telephone_ext):
        self.telephone_ext = telephone_ext
    def get_receive_email_updates_flag(self):
        return self.receive_email_updates_flag
    def set_receive_email_updates_flag(self, receive_email_updates_flag):
        self.receive_email_updates_flag = receive_email_updates_flag
    def validate_contact_nameType(self, value):
        result = True
        # Validate type contact-nameType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 45:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contact-nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_EmailType(self, value):
        result = True
        # Validate type EmailType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EmailType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EmailType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EmailType_patterns_, ))
                result = False
        return result
    validate_EmailType_patterns_ = [["^((['_A-Za-z0-9\\-\\+]+)(\\.['_A-Za-z0-9\\-\\+]+)*@([A-Za-z0-9\\-]+)(\\.[A-Za-z0-9\\-]+)*(\\.[A-Za-z]{2,5}))$"]]
    def validate_PhoneType(self, value):
        result = True
        # Validate type PhoneType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PhoneType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_PhoneType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PhoneType_patterns_, ))
                result = False
        return result
    validate_PhoneType_patterns_ = [['^([0-9]{3}-[0-9]{3}-[0-9]{4})$']]
    def validate_PhoneExtentionType(self, value):
        result = True
        # Validate type PhoneExtentionType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PhoneExtentionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PhoneExtentionType_patterns_, ))
                result = False
        return result
    validate_PhoneExtentionType_patterns_ = [['^(\\d{1,6})$']]
    def _hasContent(self):
        if (
            self.contact_name is not None or
            self.email is not None or
            self.contact_phone is not None or
            self.telephone_ext is not None or
            self.receive_email_updates_flag is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ContactInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ContactInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ContactInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ContactInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ContactInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.contact_name is not None:
            namespaceprefix_ = self.contact_name_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontact-name>%s</%scontact-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contact_name), input_name='contact-name')), namespaceprefix_ , eol_))
        if self.email is not None:
            namespaceprefix_ = self.email_nsprefix_ + ':' if (UseCapturedNS_ and self.email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semail>%s</%semail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.email), input_name='email')), namespaceprefix_ , eol_))
        if self.contact_phone is not None:
            namespaceprefix_ = self.contact_phone_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontact-phone>%s</%scontact-phone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contact_phone), input_name='contact-phone')), namespaceprefix_ , eol_))
        if self.telephone_ext is not None:
            namespaceprefix_ = self.telephone_ext_nsprefix_ + ':' if (UseCapturedNS_ and self.telephone_ext_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stelephone-ext>%s</%stelephone-ext>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.telephone_ext), input_name='telephone-ext')), namespaceprefix_ , eol_))
        if self.receive_email_updates_flag is not None:
            namespaceprefix_ = self.receive_email_updates_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.receive_email_updates_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreceive-email-updates-flag>%s</%sreceive-email-updates-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.receive_email_updates_flag, input_name='receive-email-updates-flag'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'contact-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contact_name')
            value_ = self.gds_validate_string(value_, node, 'contact_name')
            self.contact_name = value_
            self.contact_name_nsprefix_ = child_.prefix
            # validate type contact-nameType
            self.validate_contact_nameType(self.contact_name)
        elif nodeName_ == 'email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'email')
            value_ = self.gds_validate_string(value_, node, 'email')
            self.email = value_
            self.email_nsprefix_ = child_.prefix
            # validate type EmailType
            self.validate_EmailType(self.email)
        elif nodeName_ == 'contact-phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contact_phone')
            value_ = self.gds_validate_string(value_, node, 'contact_phone')
            self.contact_phone = value_
            self.contact_phone_nsprefix_ = child_.prefix
            # validate type PhoneType
            self.validate_PhoneType(self.contact_phone)
        elif nodeName_ == 'telephone-ext':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'telephone_ext')
            value_ = self.gds_validate_string(value_, node, 'telephone_ext')
            self.telephone_ext = value_
            self.telephone_ext_nsprefix_ = child_.prefix
            # validate type PhoneExtentionType
            self.validate_PhoneExtentionType(self.telephone_ext)
        elif nodeName_ == 'receive-email-updates-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'receive_email_updates_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'receive_email_updates_flag')
            self.receive_email_updates_flag = ival_
            self.receive_email_updates_flag_nsprefix_ = child_.prefix
# end class ContactInfoType


class ContactInfoResponseDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, contact_name=None, email=None, contact_phone=None, telephone_ext=None, receive_email_updates_flag=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.contact_name = contact_name
        self.validate_contact_nameType2(self.contact_name)
        self.contact_name_nsprefix_ = None
        self.email = email
        self.validate_EmailType(self.email)
        self.email_nsprefix_ = None
        self.contact_phone = contact_phone
        self.validate_PhoneType(self.contact_phone)
        self.contact_phone_nsprefix_ = None
        self.telephone_ext = telephone_ext
        self.validate_PhoneExtentionType(self.telephone_ext)
        self.telephone_ext_nsprefix_ = None
        self.receive_email_updates_flag = receive_email_updates_flag
        self.receive_email_updates_flag_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ContactInfoResponseDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ContactInfoResponseDetailsType.subclass:
            return ContactInfoResponseDetailsType.subclass(*args_, **kwargs_)
        else:
            return ContactInfoResponseDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contact_name(self):
        return self.contact_name
    def set_contact_name(self, contact_name):
        self.contact_name = contact_name
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def get_contact_phone(self):
        return self.contact_phone
    def set_contact_phone(self, contact_phone):
        self.contact_phone = contact_phone
    def get_telephone_ext(self):
        return self.telephone_ext
    def set_telephone_ext(self, telephone_ext):
        self.telephone_ext = telephone_ext
    def get_receive_email_updates_flag(self):
        return self.receive_email_updates_flag
    def set_receive_email_updates_flag(self, receive_email_updates_flag):
        self.receive_email_updates_flag = receive_email_updates_flag
    def validate_contact_nameType2(self, value):
        result = True
        # Validate type contact-nameType2, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 45:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contact-nameType2' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_EmailType(self, value):
        result = True
        # Validate type EmailType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on EmailType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_EmailType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_EmailType_patterns_, ))
                result = False
        return result
    validate_EmailType_patterns_ = [["^((['_A-Za-z0-9\\-\\+]+)(\\.['_A-Za-z0-9\\-\\+]+)*@([A-Za-z0-9\\-]+)(\\.[A-Za-z0-9\\-]+)*(\\.[A-Za-z]{2,5}))$"]]
    def validate_PhoneType(self, value):
        result = True
        # Validate type PhoneType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PhoneType' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_PhoneType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PhoneType_patterns_, ))
                result = False
        return result
    validate_PhoneType_patterns_ = [['^([0-9]{3}-[0-9]{3}-[0-9]{4})$']]
    def validate_PhoneExtentionType(self, value):
        result = True
        # Validate type PhoneExtentionType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PhoneExtentionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PhoneExtentionType_patterns_, ))
                result = False
        return result
    validate_PhoneExtentionType_patterns_ = [['^(\\d{1,6})$']]
    def _hasContent(self):
        if (
            self.contact_name is not None or
            self.email is not None or
            self.contact_phone is not None or
            self.telephone_ext is not None or
            self.receive_email_updates_flag is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactInfoResponseDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ContactInfoResponseDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ContactInfoResponseDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ContactInfoResponseDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ContactInfoResponseDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ContactInfoResponseDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ContactInfoResponseDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.contact_name is not None:
            namespaceprefix_ = self.contact_name_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontact-name>%s</%scontact-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contact_name), input_name='contact-name')), namespaceprefix_ , eol_))
        if self.email is not None:
            namespaceprefix_ = self.email_nsprefix_ + ':' if (UseCapturedNS_ and self.email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semail>%s</%semail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.email), input_name='email')), namespaceprefix_ , eol_))
        if self.contact_phone is not None:
            namespaceprefix_ = self.contact_phone_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontact-phone>%s</%scontact-phone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contact_phone), input_name='contact-phone')), namespaceprefix_ , eol_))
        if self.telephone_ext is not None:
            namespaceprefix_ = self.telephone_ext_nsprefix_ + ':' if (UseCapturedNS_ and self.telephone_ext_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stelephone-ext>%s</%stelephone-ext>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.telephone_ext), input_name='telephone-ext')), namespaceprefix_ , eol_))
        if self.receive_email_updates_flag is not None:
            namespaceprefix_ = self.receive_email_updates_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.receive_email_updates_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreceive-email-updates-flag>%s</%sreceive-email-updates-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.receive_email_updates_flag, input_name='receive-email-updates-flag'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'contact-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contact_name')
            value_ = self.gds_validate_string(value_, node, 'contact_name')
            self.contact_name = value_
            self.contact_name_nsprefix_ = child_.prefix
            # validate type contact-nameType2
            self.validate_contact_nameType2(self.contact_name)
        elif nodeName_ == 'email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'email')
            value_ = self.gds_validate_string(value_, node, 'email')
            self.email = value_
            self.email_nsprefix_ = child_.prefix
            # validate type EmailType
            self.validate_EmailType(self.email)
        elif nodeName_ == 'contact-phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contact_phone')
            value_ = self.gds_validate_string(value_, node, 'contact_phone')
            self.contact_phone = value_
            self.contact_phone_nsprefix_ = child_.prefix
            # validate type PhoneType
            self.validate_PhoneType(self.contact_phone)
        elif nodeName_ == 'telephone-ext':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'telephone_ext')
            value_ = self.gds_validate_string(value_, node, 'telephone_ext')
            self.telephone_ext = value_
            self.telephone_ext_nsprefix_ = child_.prefix
            # validate type PhoneExtentionType
            self.validate_PhoneExtentionType(self.telephone_ext)
        elif nodeName_ == 'receive-email-updates-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'receive_email_updates_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'receive_email_updates_flag')
            self.receive_email_updates_flag = ival_
            self.receive_email_updates_flag_nsprefix_ = child_.prefix
# end class ContactInfoResponseDetailsType


class LocationDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, five_ton_flag=None, loading_dock_flag=None, pickup_instructions=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.five_ton_flag = five_ton_flag
        self.five_ton_flag_nsprefix_ = None
        self.loading_dock_flag = loading_dock_flag
        self.loading_dock_flag_nsprefix_ = None
        self.pickup_instructions = pickup_instructions
        self.validate_pickup_instructionsType(self.pickup_instructions)
        self.pickup_instructions_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LocationDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LocationDetailsType.subclass:
            return LocationDetailsType.subclass(*args_, **kwargs_)
        else:
            return LocationDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_five_ton_flag(self):
        return self.five_ton_flag
    def set_five_ton_flag(self, five_ton_flag):
        self.five_ton_flag = five_ton_flag
    def get_loading_dock_flag(self):
        return self.loading_dock_flag
    def set_loading_dock_flag(self, loading_dock_flag):
        self.loading_dock_flag = loading_dock_flag
    def get_pickup_instructions(self):
        return self.pickup_instructions
    def set_pickup_instructions(self, pickup_instructions):
        self.pickup_instructions = pickup_instructions
    def validate_pickup_instructionsType(self, value):
        result = True
        # Validate type pickup-instructionsType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 132:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on pickup-instructionsType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.five_ton_flag is not None or
            self.loading_dock_flag is not None or
            self.pickup_instructions is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LocationDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LocationDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LocationDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LocationDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LocationDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LocationDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LocationDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.five_ton_flag is not None:
            namespaceprefix_ = self.five_ton_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.five_ton_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfive-ton-flag>%s</%sfive-ton-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.five_ton_flag, input_name='five-ton-flag'), namespaceprefix_ , eol_))
        if self.loading_dock_flag is not None:
            namespaceprefix_ = self.loading_dock_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.loading_dock_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sloading-dock-flag>%s</%sloading-dock-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.loading_dock_flag, input_name='loading-dock-flag'), namespaceprefix_ , eol_))
        if self.pickup_instructions is not None:
            namespaceprefix_ = self.pickup_instructions_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_instructions_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-instructions>%s</%spickup-instructions>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_instructions), input_name='pickup-instructions')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'five-ton-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'five_ton_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'five_ton_flag')
            self.five_ton_flag = ival_
            self.five_ton_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'loading-dock-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'loading_dock_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'loading_dock_flag')
            self.loading_dock_flag = ival_
            self.loading_dock_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'pickup-instructions':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_instructions')
            value_ = self.gds_validate_string(value_, node, 'pickup_instructions')
            self.pickup_instructions = value_
            self.pickup_instructions_nsprefix_ = child_.prefix
            # validate type pickup-instructionsType
            self.validate_pickup_instructionsType(self.pickup_instructions)
# end class LocationDetailsType


class ItemsCharacteristicsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pww_flag=None, priority_flag=None, returns_flag=None, heavy_item_flag=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pww_flag = pww_flag
        self.pww_flag_nsprefix_ = None
        self.priority_flag = priority_flag
        self.priority_flag_nsprefix_ = None
        self.returns_flag = returns_flag
        self.returns_flag_nsprefix_ = None
        self.heavy_item_flag = heavy_item_flag
        self.heavy_item_flag_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ItemsCharacteristicsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ItemsCharacteristicsType.subclass:
            return ItemsCharacteristicsType.subclass(*args_, **kwargs_)
        else:
            return ItemsCharacteristicsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pww_flag(self):
        return self.pww_flag
    def set_pww_flag(self, pww_flag):
        self.pww_flag = pww_flag
    def get_priority_flag(self):
        return self.priority_flag
    def set_priority_flag(self, priority_flag):
        self.priority_flag = priority_flag
    def get_returns_flag(self):
        return self.returns_flag
    def set_returns_flag(self, returns_flag):
        self.returns_flag = returns_flag
    def get_heavy_item_flag(self):
        return self.heavy_item_flag
    def set_heavy_item_flag(self, heavy_item_flag):
        self.heavy_item_flag = heavy_item_flag
    def _hasContent(self):
        if (
            self.pww_flag is not None or
            self.priority_flag is not None or
            self.returns_flag is not None or
            self.heavy_item_flag is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemsCharacteristicsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ItemsCharacteristicsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ItemsCharacteristicsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ItemsCharacteristicsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ItemsCharacteristicsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ItemsCharacteristicsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemsCharacteristicsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pww_flag is not None:
            namespaceprefix_ = self.pww_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.pww_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spww-flag>%s</%spww-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.pww_flag, input_name='pww-flag'), namespaceprefix_ , eol_))
        if self.priority_flag is not None:
            namespaceprefix_ = self.priority_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.priority_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spriority-flag>%s</%spriority-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.priority_flag, input_name='priority-flag'), namespaceprefix_ , eol_))
        if self.returns_flag is not None:
            namespaceprefix_ = self.returns_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.returns_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreturns-flag>%s</%sreturns-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.returns_flag, input_name='returns-flag'), namespaceprefix_ , eol_))
        if self.heavy_item_flag is not None:
            namespaceprefix_ = self.heavy_item_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.heavy_item_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sheavy-item-flag>%s</%sheavy-item-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.heavy_item_flag, input_name='heavy-item-flag'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'pww-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'pww_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'pww_flag')
            self.pww_flag = ival_
            self.pww_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'priority-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'priority_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'priority_flag')
            self.priority_flag = ival_
            self.priority_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'returns-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'returns_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'returns_flag')
            self.returns_flag = ival_
            self.returns_flag_nsprefix_ = child_.prefix
        elif nodeName_ == 'heavy-item-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'heavy_item_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'heavy_item_flag')
            self.heavy_item_flag = ival_
            self.heavy_item_flag_nsprefix_ = child_.prefix
# end class ItemsCharacteristicsType


class ItemsCharacteristicsUpdateDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, heavy_item_flag=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.heavy_item_flag = heavy_item_flag
        self.heavy_item_flag_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ItemsCharacteristicsUpdateDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ItemsCharacteristicsUpdateDetailsType.subclass:
            return ItemsCharacteristicsUpdateDetailsType.subclass(*args_, **kwargs_)
        else:
            return ItemsCharacteristicsUpdateDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_heavy_item_flag(self):
        return self.heavy_item_flag
    def set_heavy_item_flag(self, heavy_item_flag):
        self.heavy_item_flag = heavy_item_flag
    def _hasContent(self):
        if (
            self.heavy_item_flag is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemsCharacteristicsUpdateDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ItemsCharacteristicsUpdateDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ItemsCharacteristicsUpdateDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ItemsCharacteristicsUpdateDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ItemsCharacteristicsUpdateDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ItemsCharacteristicsUpdateDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ItemsCharacteristicsUpdateDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.heavy_item_flag is not None:
            namespaceprefix_ = self.heavy_item_flag_nsprefix_ + ':' if (UseCapturedNS_ and self.heavy_item_flag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sheavy-item-flag>%s</%sheavy-item-flag>%s' % (namespaceprefix_ , self.gds_format_boolean(self.heavy_item_flag, input_name='heavy-item-flag'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'heavy-item-flag':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'heavy_item_flag')
            ival_ = self.gds_validate_boolean(ival_, node, 'heavy_item_flag')
            self.heavy_item_flag = ival_
            self.heavy_item_flag_nsprefix_ = child_.prefix
# end class ItemsCharacteristicsUpdateDetailsType


class PickupTimesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, on_demand_pickup_time=None, scheduled_pickup_times=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.on_demand_pickup_time = on_demand_pickup_time
        self.on_demand_pickup_time_nsprefix_ = None
        self.scheduled_pickup_times = scheduled_pickup_times
        self.scheduled_pickup_times_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupTimesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupTimesType.subclass:
            return PickupTimesType.subclass(*args_, **kwargs_)
        else:
            return PickupTimesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_on_demand_pickup_time(self):
        return self.on_demand_pickup_time
    def set_on_demand_pickup_time(self, on_demand_pickup_time):
        self.on_demand_pickup_time = on_demand_pickup_time
    def get_scheduled_pickup_times(self):
        return self.scheduled_pickup_times
    def set_scheduled_pickup_times(self, scheduled_pickup_times):
        self.scheduled_pickup_times = scheduled_pickup_times
    def _hasContent(self):
        if (
            self.on_demand_pickup_time is not None or
            self.scheduled_pickup_times is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupTimesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupTimesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupTimesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupTimesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupTimesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupTimesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupTimesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.on_demand_pickup_time is not None:
            namespaceprefix_ = self.on_demand_pickup_time_nsprefix_ + ':' if (UseCapturedNS_ and self.on_demand_pickup_time_nsprefix_) else ''
            self.on_demand_pickup_time.export(outfile, level, namespaceprefix_, namespacedef_='', name_='on-demand-pickup-time', pretty_print=pretty_print)
        if self.scheduled_pickup_times is not None:
            namespaceprefix_ = self.scheduled_pickup_times_nsprefix_ + ':' if (UseCapturedNS_ and self.scheduled_pickup_times_nsprefix_) else ''
            self.scheduled_pickup_times.export(outfile, level, namespaceprefix_, namespacedef_='', name_='scheduled-pickup-times', pretty_print=pretty_print)
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
        if nodeName_ == 'on-demand-pickup-time':
            obj_ = OnDemandPickupTimeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.on_demand_pickup_time = obj_
            obj_.original_tagname_ = 'on-demand-pickup-time'
        elif nodeName_ == 'scheduled-pickup-times':
            obj_ = ScheduledPickupTimesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.scheduled_pickup_times = obj_
            obj_.original_tagname_ = 'scheduled-pickup-times'
# end class PickupTimesType


class OnDemandPickupTimeType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, date=None, preferred_time=None, closing_time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if isinstance(date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            initvalue_ = date
        self.date = initvalue_
        self.date_nsprefix_ = None
        self.preferred_time = preferred_time
        self.validate_PickupTimeType(self.preferred_time)
        self.preferred_time_nsprefix_ = None
        self.closing_time = closing_time
        self.validate_PickupTimeType(self.closing_time)
        self.closing_time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OnDemandPickupTimeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OnDemandPickupTimeType.subclass:
            return OnDemandPickupTimeType.subclass(*args_, **kwargs_)
        else:
            return OnDemandPickupTimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def get_preferred_time(self):
        return self.preferred_time
    def set_preferred_time(self, preferred_time):
        self.preferred_time = preferred_time
    def get_closing_time(self):
        return self.closing_time
    def set_closing_time(self, closing_time):
        self.closing_time = closing_time
    def validate_PickupTimeType(self, value):
        result = True
        # Validate type PickupTimeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PickupTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PickupTimeType_patterns_, ))
                result = False
        return result
    validate_PickupTimeType_patterns_ = [['^((12|13|14|15|16|17):(00|15|30|45))$']]
    def _hasContent(self):
        if (
            self.date is not None or
            self.preferred_time is not None or
            self.closing_time is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OnDemandPickupTimeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OnDemandPickupTimeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OnDemandPickupTimeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OnDemandPickupTimeType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OnDemandPickupTimeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OnDemandPickupTimeType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='OnDemandPickupTimeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.date is not None:
            namespaceprefix_ = self.date_nsprefix_ + ':' if (UseCapturedNS_ and self.date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdate>%s</%sdate>%s' % (namespaceprefix_ , self.gds_format_date(self.date, input_name='date'), namespaceprefix_ , eol_))
        if self.preferred_time is not None:
            namespaceprefix_ = self.preferred_time_nsprefix_ + ':' if (UseCapturedNS_ and self.preferred_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spreferred-time>%s</%spreferred-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.preferred_time), input_name='preferred-time')), namespaceprefix_ , eol_))
        if self.closing_time is not None:
            namespaceprefix_ = self.closing_time_nsprefix_ + ':' if (UseCapturedNS_ and self.closing_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclosing-time>%s</%sclosing-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.closing_time), input_name='closing-time')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.date = dval_
            self.date_nsprefix_ = child_.prefix
        elif nodeName_ == 'preferred-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'preferred_time')
            value_ = self.gds_validate_string(value_, node, 'preferred_time')
            self.preferred_time = value_
            self.preferred_time_nsprefix_ = child_.prefix
            # validate type PickupTimeType
            self.validate_PickupTimeType(self.preferred_time)
        elif nodeName_ == 'closing-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'closing_time')
            value_ = self.gds_validate_string(value_, node, 'closing_time')
            self.closing_time = value_
            self.closing_time_nsprefix_ = child_.prefix
            # validate type PickupTimeType
            self.validate_PickupTimeType(self.closing_time)
# end class OnDemandPickupTimeType


class ScheduledPickupTimesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pickup_times_per_day=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if pickup_times_per_day is None:
            self.pickup_times_per_day = []
        else:
            self.pickup_times_per_day = pickup_times_per_day
        self.pickup_times_per_day_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ScheduledPickupTimesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ScheduledPickupTimesType.subclass:
            return ScheduledPickupTimesType.subclass(*args_, **kwargs_)
        else:
            return ScheduledPickupTimesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pickup_times_per_day(self):
        return self.pickup_times_per_day
    def set_pickup_times_per_day(self, pickup_times_per_day):
        self.pickup_times_per_day = pickup_times_per_day
    def add_pickup_times_per_day(self, value):
        self.pickup_times_per_day.append(value)
    def insert_pickup_times_per_day_at(self, index, value):
        self.pickup_times_per_day.insert(index, value)
    def replace_pickup_times_per_day_at(self, index, value):
        self.pickup_times_per_day[index] = value
    def _hasContent(self):
        if (
            self.pickup_times_per_day
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ScheduledPickupTimesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ScheduledPickupTimesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ScheduledPickupTimesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ScheduledPickupTimesType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ScheduledPickupTimesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ScheduledPickupTimesType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ScheduledPickupTimesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for pickup_times_per_day_ in self.pickup_times_per_day:
            namespaceprefix_ = self.pickup_times_per_day_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_times_per_day_nsprefix_) else ''
            pickup_times_per_day_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pickup-times-per-day', pretty_print=pretty_print)
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
        if nodeName_ == 'pickup-times-per-day':
            obj_ = PickupTimesPerDayType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pickup_times_per_day.append(obj_)
            obj_.original_tagname_ = 'pickup-times-per-day'
# end class ScheduledPickupTimesType


class PickupTimesPerDayType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, day=None, preferred_time_1=None, preferred_time_2=None, closing_time=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.day = day
        self.validate_DayOfTheWeekType(self.day)
        self.day_nsprefix_ = None
        self.preferred_time_1 = preferred_time_1
        self.validate_PickupTimeType(self.preferred_time_1)
        self.preferred_time_1_nsprefix_ = None
        self.preferred_time_2 = preferred_time_2
        self.validate_PickupTimeType(self.preferred_time_2)
        self.preferred_time_2_nsprefix_ = None
        self.closing_time = closing_time
        self.validate_PickupTimeType(self.closing_time)
        self.closing_time_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupTimesPerDayType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupTimesPerDayType.subclass:
            return PickupTimesPerDayType.subclass(*args_, **kwargs_)
        else:
            return PickupTimesPerDayType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_day(self):
        return self.day
    def set_day(self, day):
        self.day = day
    def get_preferred_time_1(self):
        return self.preferred_time_1
    def set_preferred_time_1(self, preferred_time_1):
        self.preferred_time_1 = preferred_time_1
    def get_preferred_time_2(self):
        return self.preferred_time_2
    def set_preferred_time_2(self, preferred_time_2):
        self.preferred_time_2 = preferred_time_2
    def get_closing_time(self):
        return self.closing_time
    def set_closing_time(self, closing_time):
        self.closing_time = closing_time
    def validate_DayOfTheWeekType(self, value):
        result = True
        # Validate type DayOfTheWeekType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['MON', 'TUE', 'WED', 'THU', 'FRI']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DayOfTheWeekType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_PickupTimeType(self, value):
        result = True
        # Validate type PickupTimeType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PickupTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PickupTimeType_patterns_, ))
                result = False
        return result
    validate_PickupTimeType_patterns_ = [['^((12|13|14|15|16|17):(00|15|30|45))$']]
    def _hasContent(self):
        if (
            self.day is not None or
            self.preferred_time_1 is not None or
            self.preferred_time_2 is not None or
            self.closing_time is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupTimesPerDayType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupTimesPerDayType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupTimesPerDayType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupTimesPerDayType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupTimesPerDayType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupTimesPerDayType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupTimesPerDayType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.day is not None:
            namespaceprefix_ = self.day_nsprefix_ + ':' if (UseCapturedNS_ and self.day_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sday>%s</%sday>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.day), input_name='day')), namespaceprefix_ , eol_))
        if self.preferred_time_1 is not None:
            namespaceprefix_ = self.preferred_time_1_nsprefix_ + ':' if (UseCapturedNS_ and self.preferred_time_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spreferred-time-1>%s</%spreferred-time-1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.preferred_time_1), input_name='preferred-time-1')), namespaceprefix_ , eol_))
        if self.preferred_time_2 is not None:
            namespaceprefix_ = self.preferred_time_2_nsprefix_ + ':' if (UseCapturedNS_ and self.preferred_time_2_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spreferred-time-2>%s</%spreferred-time-2>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.preferred_time_2), input_name='preferred-time-2')), namespaceprefix_ , eol_))
        if self.closing_time is not None:
            namespaceprefix_ = self.closing_time_nsprefix_ + ':' if (UseCapturedNS_ and self.closing_time_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclosing-time>%s</%sclosing-time>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.closing_time), input_name='closing-time')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'day':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'day')
            value_ = self.gds_validate_string(value_, node, 'day')
            self.day = value_
            self.day_nsprefix_ = child_.prefix
            # validate type DayOfTheWeekType
            self.validate_DayOfTheWeekType(self.day)
        elif nodeName_ == 'preferred-time-1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'preferred_time_1')
            value_ = self.gds_validate_string(value_, node, 'preferred_time_1')
            self.preferred_time_1 = value_
            self.preferred_time_1_nsprefix_ = child_.prefix
            # validate type PickupTimeType
            self.validate_PickupTimeType(self.preferred_time_1)
        elif nodeName_ == 'preferred-time-2':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'preferred_time_2')
            value_ = self.gds_validate_string(value_, node, 'preferred_time_2')
            self.preferred_time_2 = value_
            self.preferred_time_2_nsprefix_ = child_.prefix
            # validate type PickupTimeType
            self.validate_PickupTimeType(self.preferred_time_2)
        elif nodeName_ == 'closing-time':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'closing_time')
            value_ = self.gds_validate_string(value_, node, 'closing_time')
            self.closing_time = value_
            self.closing_time_nsprefix_ = child_.prefix
            # validate type PickupTimeType
            self.validate_PickupTimeType(self.closing_time)
# end class PickupTimesPerDayType


class PaymentInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, contract_id=None, method_of_payment=None, pre_authorized_payment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.contract_id = contract_id
        self.validate_ContractIDType(self.contract_id)
        self.contract_id_nsprefix_ = None
        self.method_of_payment = method_of_payment
        self.validate_MethodOfPaymentType(self.method_of_payment)
        self.method_of_payment_nsprefix_ = None
        self.pre_authorized_payment = pre_authorized_payment
        self.pre_authorized_payment_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PaymentInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PaymentInfoType.subclass:
            return PaymentInfoType.subclass(*args_, **kwargs_)
        else:
            return PaymentInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_contract_id(self):
        return self.contract_id
    def set_contract_id(self, contract_id):
        self.contract_id = contract_id
    def get_method_of_payment(self):
        return self.method_of_payment
    def set_method_of_payment(self, method_of_payment):
        self.method_of_payment = method_of_payment
    def get_pre_authorized_payment(self):
        return self.pre_authorized_payment
    def set_pre_authorized_payment(self, pre_authorized_payment):
        self.pre_authorized_payment = pre_authorized_payment
    def validate_ContractIDType(self, value):
        result = True
        # Validate type ContractIDType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_ContractIDType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ContractIDType_patterns_, ))
                result = False
        return result
    validate_ContractIDType_patterns_ = [['^(\\d{1,10})$']]
    def validate_MethodOfPaymentType(self, value):
        result = True
        # Validate type MethodOfPaymentType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CreditCard', 'Account', 'SupplierAccount']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MethodOfPaymentType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.contract_id is not None or
            self.method_of_payment is not None or
            self.pre_authorized_payment is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PaymentInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PaymentInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PaymentInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PaymentInfoType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PaymentInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PaymentInfoType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PaymentInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.contract_id is not None:
            namespaceprefix_ = self.contract_id_nsprefix_ + ':' if (UseCapturedNS_ and self.contract_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scontract-id>%s</%scontract-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.contract_id), input_name='contract-id')), namespaceprefix_ , eol_))
        if self.method_of_payment is not None:
            namespaceprefix_ = self.method_of_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.method_of_payment_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smethod-of-payment>%s</%smethod-of-payment>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.method_of_payment), input_name='method-of-payment')), namespaceprefix_ , eol_))
        if self.pre_authorized_payment is not None:
            namespaceprefix_ = self.pre_authorized_payment_nsprefix_ + ':' if (UseCapturedNS_ and self.pre_authorized_payment_nsprefix_) else ''
            self.pre_authorized_payment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pre-authorized-payment', pretty_print=pretty_print)
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
        if nodeName_ == 'contract-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contract_id')
            value_ = self.gds_validate_string(value_, node, 'contract_id')
            self.contract_id = value_
            self.contract_id_nsprefix_ = child_.prefix
            # validate type ContractIDType
            self.validate_ContractIDType(self.contract_id)
        elif nodeName_ == 'method-of-payment':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'method_of_payment')
            value_ = self.gds_validate_string(value_, node, 'method_of_payment')
            self.method_of_payment = value_
            self.method_of_payment_nsprefix_ = child_.prefix
            # validate type MethodOfPaymentType
            self.validate_MethodOfPaymentType(self.method_of_payment)
        elif nodeName_ == 'pre-authorized-payment':
            obj_ = PreAuthorizedPaymentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pre_authorized_payment = obj_
            obj_.original_tagname_ = 'pre-authorized-payment'
# end class PaymentInfoType


class PreAuthorizedPaymentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, account_number=None, auth_code=None, auth_timestamp=None, charge_amount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.account_number = account_number
        self.validate_PreAuthorizedPaymentAccountNumberType(self.account_number)
        self.account_number_nsprefix_ = None
        self.auth_code = auth_code
        self.validate_PreAuthorizedPaymentAuthCodeType(self.auth_code)
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.charge_amount = charge_amount
        self.validate_PreAuthorizedPaymentAmountType(self.charge_amount)
        self.charge_amount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PreAuthorizedPaymentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PreAuthorizedPaymentType.subclass:
            return PreAuthorizedPaymentType.subclass(*args_, **kwargs_)
        else:
            return PreAuthorizedPaymentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_account_number(self):
        return self.account_number
    def set_account_number(self, account_number):
        self.account_number = account_number
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_charge_amount(self):
        return self.charge_amount
    def set_charge_amount(self, charge_amount):
        self.charge_amount = charge_amount
    def validate_PreAuthorizedPaymentAccountNumberType(self, value):
        result = True
        # Validate type PreAuthorizedPaymentAccountNumberType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PreAuthorizedPaymentAccountNumberType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PreAuthorizedPaymentAccountNumberType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PreAuthorizedPaymentAuthCodeType(self, value):
        result = True
        # Validate type PreAuthorizedPaymentAuthCodeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PreAuthorizedPaymentAuthCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PreAuthorizedPaymentAuthCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PreAuthorizedPaymentAmountType(self, value):
        result = True
        # Validate type PreAuthorizedPaymentAmountType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on PreAuthorizedPaymentAmountType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 9999999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on PreAuthorizedPaymentAmountType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.account_number is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.charge_amount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreAuthorizedPaymentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PreAuthorizedPaymentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PreAuthorizedPaymentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PreAuthorizedPaymentType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PreAuthorizedPaymentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PreAuthorizedPaymentType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PreAuthorizedPaymentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.account_number is not None:
            namespaceprefix_ = self.account_number_nsprefix_ + ':' if (UseCapturedNS_ and self.account_number_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saccount-number>%s</%saccount-number>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.account_number), input_name='account-number')), namespaceprefix_ , eol_))
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.charge_amount is not None:
            namespaceprefix_ = self.charge_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.charge_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scharge-amount>%s</%scharge-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.charge_amount, input_name='charge-amount'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'account-number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'account_number')
            value_ = self.gds_validate_string(value_, node, 'account_number')
            self.account_number = value_
            self.account_number_nsprefix_ = child_.prefix
            # validate type PreAuthorizedPaymentAccountNumberType
            self.validate_PreAuthorizedPaymentAccountNumberType(self.account_number)
        elif nodeName_ == 'auth-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'auth_code')
            value_ = self.gds_validate_string(value_, node, 'auth_code')
            self.auth_code = value_
            self.auth_code_nsprefix_ = child_.prefix
            # validate type PreAuthorizedPaymentAuthCodeType
            self.validate_PreAuthorizedPaymentAuthCodeType(self.auth_code)
        elif nodeName_ == 'auth-timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.auth_timestamp = dval_
            self.auth_timestamp_nsprefix_ = child_.prefix
        elif nodeName_ == 'charge-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'charge_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'charge_amount')
            self.charge_amount = fval_
            self.charge_amount_nsprefix_ = child_.prefix
            # validate type PreAuthorizedPaymentAmountType
            self.validate_PreAuthorizedPaymentAmountType(self.charge_amount)
# end class PreAuthorizedPaymentType


class PickupRequestHeaderType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, request_id=None, request_status=None, pickup_type=None, request_date=None, next_pickup_date=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.request_id = request_id
        self.validate_RequestIDType(self.request_id)
        self.request_id_nsprefix_ = None
        self.request_status = request_status
        self.validate_PickupStatusType(self.request_status)
        self.request_status_nsprefix_ = None
        self.pickup_type = pickup_type
        self.validate_PickupTypeType(self.pickup_type)
        self.pickup_type_nsprefix_ = None
        if isinstance(request_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(request_date, '%Y-%m-%d').date()
        else:
            initvalue_ = request_date
        self.request_date = initvalue_
        self.request_date_nsprefix_ = None
        if isinstance(next_pickup_date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(next_pickup_date, '%Y-%m-%d').date()
        else:
            initvalue_ = next_pickup_date
        self.next_pickup_date = initvalue_
        self.next_pickup_date_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestHeaderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestHeaderType.subclass:
            return PickupRequestHeaderType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_request_id(self):
        return self.request_id
    def set_request_id(self, request_id):
        self.request_id = request_id
    def get_request_status(self):
        return self.request_status
    def set_request_status(self, request_status):
        self.request_status = request_status
    def get_pickup_type(self):
        return self.pickup_type
    def set_pickup_type(self, pickup_type):
        self.pickup_type = pickup_type
    def get_request_date(self):
        return self.request_date
    def set_request_date(self, request_date):
        self.request_date = request_date
    def get_next_pickup_date(self):
        return self.next_pickup_date
    def set_next_pickup_date(self, next_pickup_date):
        self.next_pickup_date = next_pickup_date
    def validate_RequestIDType(self, value):
        result = True
        # Validate type RequestIDType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RequestIDType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on RequestIDType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_PickupStatusType(self, value):
        result = True
        # Validate type PickupStatusType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Active', 'New', 'Cancelled', 'Pending', 'Missed Pickup']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PickupStatusType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_PickupTypeType(self, value):
        result = True
        # Validate type PickupTypeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['OnDemand', 'Scheduled']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PickupTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.request_id is not None or
            self.request_status is not None or
            self.pickup_type is not None or
            self.request_date is not None or
            self.next_pickup_date is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestHeaderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestHeaderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestHeaderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestHeaderType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestHeaderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestHeaderType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.request_id is not None:
            namespaceprefix_ = self.request_id_nsprefix_ + ':' if (UseCapturedNS_ and self.request_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequest-id>%s</%srequest-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.request_id), input_name='request-id')), namespaceprefix_ , eol_))
        if self.request_status is not None:
            namespaceprefix_ = self.request_status_nsprefix_ + ':' if (UseCapturedNS_ and self.request_status_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequest-status>%s</%srequest-status>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.request_status), input_name='request-status')), namespaceprefix_ , eol_))
        if self.pickup_type is not None:
            namespaceprefix_ = self.pickup_type_nsprefix_ + ':' if (UseCapturedNS_ and self.pickup_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spickup-type>%s</%spickup-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.pickup_type), input_name='pickup-type')), namespaceprefix_ , eol_))
        if self.request_date is not None:
            namespaceprefix_ = self.request_date_nsprefix_ + ':' if (UseCapturedNS_ and self.request_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srequest-date>%s</%srequest-date>%s' % (namespaceprefix_ , self.gds_format_date(self.request_date, input_name='request-date'), namespaceprefix_ , eol_))
        if self.next_pickup_date is not None:
            namespaceprefix_ = self.next_pickup_date_nsprefix_ + ':' if (UseCapturedNS_ and self.next_pickup_date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snext-pickup-date>%s</%snext-pickup-date>%s' % (namespaceprefix_ , self.gds_format_date(self.next_pickup_date, input_name='next-pickup-date'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'request-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'request_id')
            value_ = self.gds_validate_string(value_, node, 'request_id')
            self.request_id = value_
            self.request_id_nsprefix_ = child_.prefix
            # validate type RequestIDType
            self.validate_RequestIDType(self.request_id)
        elif nodeName_ == 'request-status':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'request_status')
            value_ = self.gds_validate_string(value_, node, 'request_status')
            self.request_status = value_
            self.request_status_nsprefix_ = child_.prefix
            # validate type PickupStatusType
            self.validate_PickupStatusType(self.request_status)
        elif nodeName_ == 'pickup-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pickup_type')
            value_ = self.gds_validate_string(value_, node, 'pickup_type')
            self.pickup_type = value_
            self.pickup_type_nsprefix_ = child_.prefix
            # validate type PickupTypeType
            self.validate_PickupTypeType(self.pickup_type)
        elif nodeName_ == 'request-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.request_date = dval_
            self.request_date_nsprefix_ = child_.prefix
        elif nodeName_ == 'next-pickup-date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.next_pickup_date = dval_
            self.next_pickup_date_nsprefix_ = child_.prefix
# end class PickupRequestHeaderType


class LinkType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, href=None, rel=None, index=None, media_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.href = _cast(None, href)
        self.href_nsprefix_ = None
        self.rel = _cast(None, rel)
        self.rel_nsprefix_ = None
        self.index = _cast(int, index)
        self.index_nsprefix_ = None
        self.media_type = _cast(None, media_type)
        self.media_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LinkType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LinkType.subclass:
            return LinkType.subclass(*args_, **kwargs_)
        else:
            return LinkType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_href(self):
        return self.href
    def set_href(self, href):
        self.href = href
    def get_rel(self):
        return self.rel
    def set_rel(self, rel):
        self.rel = rel
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_media_type(self):
        return self.media_type
    def set_media_type(self, media_type):
        self.media_type = media_type
    def validate_RelType(self, value):
        # Validate type RelType, a restriction on xsd:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def _hasContent(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LinkType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LinkType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LinkType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LinkType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LinkType'):
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.href), input_name='href')), ))
        if self.rel is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            outfile.write(' rel=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rel), input_name='rel')), ))
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.media_type is not None and 'media_type' not in already_processed:
            already_processed.add('media_type')
            outfile.write(' media-type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.media_type), input_name='media-type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LinkType', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
        value = find_attr_value_('rel', node)
        if value is not None and 'rel' not in already_processed:
            already_processed.add('rel')
            self.rel = value
            self.validate_RelType(self.rel)    # validate type RelType
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
            if self.index < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
        value = find_attr_value_('media-type', node)
        if value is not None and 'media-type' not in already_processed:
            already_processed.add('media-type')
            self.media_type = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class LinkType


class PickupRequestPriceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pre_tax_amount=None, gst_amount=None, pst_amount=None, hst_amount=None, due_amount=None, cc_receipt_details=None, supplier_account_receipt_details=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pre_tax_amount = pre_tax_amount
        self.validate_CostTypeAllowsZero(self.pre_tax_amount)
        self.pre_tax_amount_nsprefix_ = None
        self.gst_amount = gst_amount
        self.validate_CostTypeAllowsZero(self.gst_amount)
        self.gst_amount_nsprefix_ = None
        self.pst_amount = pst_amount
        self.validate_CostTypeAllowsZero(self.pst_amount)
        self.pst_amount_nsprefix_ = None
        self.hst_amount = hst_amount
        self.validate_CostTypeAllowsZero(self.hst_amount)
        self.hst_amount_nsprefix_ = None
        self.due_amount = due_amount
        self.validate_CostTypeAllowsZero(self.due_amount)
        self.due_amount_nsprefix_ = None
        self.cc_receipt_details = cc_receipt_details
        self.cc_receipt_details_nsprefix_ = None
        self.supplier_account_receipt_details = supplier_account_receipt_details
        self.supplier_account_receipt_details_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestPriceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestPriceType.subclass:
            return PickupRequestPriceType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestPriceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pre_tax_amount(self):
        return self.pre_tax_amount
    def set_pre_tax_amount(self, pre_tax_amount):
        self.pre_tax_amount = pre_tax_amount
    def get_gst_amount(self):
        return self.gst_amount
    def set_gst_amount(self, gst_amount):
        self.gst_amount = gst_amount
    def get_pst_amount(self):
        return self.pst_amount
    def set_pst_amount(self, pst_amount):
        self.pst_amount = pst_amount
    def get_hst_amount(self):
        return self.hst_amount
    def set_hst_amount(self, hst_amount):
        self.hst_amount = hst_amount
    def get_due_amount(self):
        return self.due_amount
    def set_due_amount(self, due_amount):
        self.due_amount = due_amount
    def get_cc_receipt_details(self):
        return self.cc_receipt_details
    def set_cc_receipt_details(self, cc_receipt_details):
        self.cc_receipt_details = cc_receipt_details
    def get_supplier_account_receipt_details(self):
        return self.supplier_account_receipt_details
    def set_supplier_account_receipt_details(self, supplier_account_receipt_details):
        self.supplier_account_receipt_details = supplier_account_receipt_details
    def validate_CostTypeAllowsZero(self, value):
        result = True
        # Validate type CostTypeAllowsZero, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on CostTypeAllowsZero' % {"value": value, "lineno": lineno} )
                result = False
            if value > 999999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on CostTypeAllowsZero' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.pre_tax_amount is not None or
            self.gst_amount is not None or
            self.pst_amount is not None or
            self.hst_amount is not None or
            self.due_amount is not None or
            self.cc_receipt_details is not None or
            self.supplier_account_receipt_details is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestPriceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestPriceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestPriceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestPriceType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestPriceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestPriceType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestPriceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pre_tax_amount is not None:
            namespaceprefix_ = self.pre_tax_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pre_tax_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spre-tax-amount>%s</%spre-tax-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.pre_tax_amount, input_name='pre-tax-amount'), namespaceprefix_ , eol_))
        if self.gst_amount is not None:
            namespaceprefix_ = self.gst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.gst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgst-amount>%s</%sgst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.gst_amount, input_name='gst-amount'), namespaceprefix_ , eol_))
        if self.pst_amount is not None:
            namespaceprefix_ = self.pst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spst-amount>%s</%spst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.pst_amount, input_name='pst-amount'), namespaceprefix_ , eol_))
        if self.hst_amount is not None:
            namespaceprefix_ = self.hst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.hst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shst-amount>%s</%shst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.hst_amount, input_name='hst-amount'), namespaceprefix_ , eol_))
        if self.due_amount is not None:
            namespaceprefix_ = self.due_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.due_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdue-amount>%s</%sdue-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.due_amount, input_name='due-amount'), namespaceprefix_ , eol_))
        if self.cc_receipt_details is not None:
            namespaceprefix_ = self.cc_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.cc_receipt_details_nsprefix_) else ''
            self.cc_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cc-receipt-details', pretty_print=pretty_print)
        if self.supplier_account_receipt_details is not None:
            namespaceprefix_ = self.supplier_account_receipt_details_nsprefix_ + ':' if (UseCapturedNS_ and self.supplier_account_receipt_details_nsprefix_) else ''
            self.supplier_account_receipt_details.export(outfile, level, namespaceprefix_, namespacedef_='', name_='supplier-account-receipt-details', pretty_print=pretty_print)
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
        if nodeName_ == 'pre-tax-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'pre_tax_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'pre_tax_amount')
            self.pre_tax_amount = fval_
            self.pre_tax_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.pre_tax_amount)
        elif nodeName_ == 'gst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'gst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'gst_amount')
            self.gst_amount = fval_
            self.gst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.gst_amount)
        elif nodeName_ == 'pst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'pst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'pst_amount')
            self.pst_amount = fval_
            self.pst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.pst_amount)
        elif nodeName_ == 'hst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'hst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'hst_amount')
            self.hst_amount = fval_
            self.hst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.hst_amount)
        elif nodeName_ == 'due-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'due_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'due_amount')
            self.due_amount = fval_
            self.due_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.due_amount)
        elif nodeName_ == 'cc-receipt-details':
            obj_ = cc_receipt_details_type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cc_receipt_details = obj_
            obj_.original_tagname_ = 'cc-receipt-details'
        elif nodeName_ == 'supplier-account-receipt-details':
            obj_ = SupplierAccountReceiptDetailsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplier_account_receipt_details = obj_
            obj_.original_tagname_ = 'supplier-account-receipt-details'
# end class PickupRequestPriceType


class PickupRequestPriceNoCCType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, pre_tax_amount=None, gst_amount=None, pst_amount=None, hst_amount=None, due_amount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pre_tax_amount = pre_tax_amount
        self.validate_CostTypeAllowsZero(self.pre_tax_amount)
        self.pre_tax_amount_nsprefix_ = None
        self.gst_amount = gst_amount
        self.validate_CostTypeAllowsZero(self.gst_amount)
        self.gst_amount_nsprefix_ = None
        self.pst_amount = pst_amount
        self.validate_CostTypeAllowsZero(self.pst_amount)
        self.pst_amount_nsprefix_ = None
        self.hst_amount = hst_amount
        self.validate_CostTypeAllowsZero(self.hst_amount)
        self.hst_amount_nsprefix_ = None
        self.due_amount = due_amount
        self.validate_CostTypeAllowsZero(self.due_amount)
        self.due_amount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PickupRequestPriceNoCCType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PickupRequestPriceNoCCType.subclass:
            return PickupRequestPriceNoCCType.subclass(*args_, **kwargs_)
        else:
            return PickupRequestPriceNoCCType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_pre_tax_amount(self):
        return self.pre_tax_amount
    def set_pre_tax_amount(self, pre_tax_amount):
        self.pre_tax_amount = pre_tax_amount
    def get_gst_amount(self):
        return self.gst_amount
    def set_gst_amount(self, gst_amount):
        self.gst_amount = gst_amount
    def get_pst_amount(self):
        return self.pst_amount
    def set_pst_amount(self, pst_amount):
        self.pst_amount = pst_amount
    def get_hst_amount(self):
        return self.hst_amount
    def set_hst_amount(self, hst_amount):
        self.hst_amount = hst_amount
    def get_due_amount(self):
        return self.due_amount
    def set_due_amount(self, due_amount):
        self.due_amount = due_amount
    def validate_CostTypeAllowsZero(self, value):
        result = True
        # Validate type CostTypeAllowsZero, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on CostTypeAllowsZero' % {"value": value, "lineno": lineno} )
                result = False
            if value > 999999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on CostTypeAllowsZero' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.pre_tax_amount is not None or
            self.gst_amount is not None or
            self.pst_amount is not None or
            self.hst_amount is not None or
            self.due_amount is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestPriceNoCCType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PickupRequestPriceNoCCType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PickupRequestPriceNoCCType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PickupRequestPriceNoCCType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PickupRequestPriceNoCCType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PickupRequestPriceNoCCType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PickupRequestPriceNoCCType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.pre_tax_amount is not None:
            namespaceprefix_ = self.pre_tax_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pre_tax_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spre-tax-amount>%s</%spre-tax-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.pre_tax_amount, input_name='pre-tax-amount'), namespaceprefix_ , eol_))
        if self.gst_amount is not None:
            namespaceprefix_ = self.gst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.gst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgst-amount>%s</%sgst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.gst_amount, input_name='gst-amount'), namespaceprefix_ , eol_))
        if self.pst_amount is not None:
            namespaceprefix_ = self.pst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.pst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spst-amount>%s</%spst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.pst_amount, input_name='pst-amount'), namespaceprefix_ , eol_))
        if self.hst_amount is not None:
            namespaceprefix_ = self.hst_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.hst_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shst-amount>%s</%shst-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.hst_amount, input_name='hst-amount'), namespaceprefix_ , eol_))
        if self.due_amount is not None:
            namespaceprefix_ = self.due_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.due_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdue-amount>%s</%sdue-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.due_amount, input_name='due-amount'), namespaceprefix_ , eol_))
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
        if nodeName_ == 'pre-tax-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'pre_tax_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'pre_tax_amount')
            self.pre_tax_amount = fval_
            self.pre_tax_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.pre_tax_amount)
        elif nodeName_ == 'gst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'gst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'gst_amount')
            self.gst_amount = fval_
            self.gst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.gst_amount)
        elif nodeName_ == 'pst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'pst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'pst_amount')
            self.pst_amount = fval_
            self.pst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.pst_amount)
        elif nodeName_ == 'hst-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'hst_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'hst_amount')
            self.hst_amount = fval_
            self.hst_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.hst_amount)
        elif nodeName_ == 'due-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'due_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'due_amount')
            self.due_amount = fval_
            self.due_amount_nsprefix_ = child_.prefix
            # validate type CostTypeAllowsZero
            self.validate_CostTypeAllowsZero(self.due_amount)
# end class PickupRequestPriceNoCCType


class SupplierAccountReceiptDetailsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, auth_code=None, auth_timestamp=None, supplier_id=None, charge_amount=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
        self.validate_merchant_nameType(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType(self.merchant_url)
        self.merchant_url_nsprefix_ = None
        self.auth_code = auth_code
        self.validate_PreAuthorizedPaymentAuthCodeType(self.auth_code)
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.supplier_id = supplier_id
        self.validate_supplier_idType(self.supplier_id)
        self.supplier_id_nsprefix_ = None
        self.charge_amount = charge_amount
        self.validate_PreAuthorizedPaymentAmountType(self.charge_amount)
        self.charge_amount_nsprefix_ = None
        self.currency = currency
        self.validate_CurrencyType(self.currency)
        self.currency_nsprefix_ = None
        self.transaction_type = transaction_type
        self.validate_transaction_typeType(self.transaction_type)
        self.transaction_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SupplierAccountReceiptDetailsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SupplierAccountReceiptDetailsType.subclass:
            return SupplierAccountReceiptDetailsType.subclass(*args_, **kwargs_)
        else:
            return SupplierAccountReceiptDetailsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_merchant_name(self):
        return self.merchant_name
    def set_merchant_name(self, merchant_name):
        self.merchant_name = merchant_name
    def get_merchant_url(self):
        return self.merchant_url
    def set_merchant_url(self, merchant_url):
        self.merchant_url = merchant_url
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_supplier_id(self):
        return self.supplier_id
    def set_supplier_id(self, supplier_id):
        self.supplier_id = supplier_id
    def get_charge_amount(self):
        return self.charge_amount
    def set_charge_amount(self, charge_amount):
        self.charge_amount = charge_amount
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def get_transaction_type(self):
        return self.transaction_type
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
    def validate_merchant_nameType(self, value):
        result = True
        # Validate type merchant-nameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 35:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-nameType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_merchant_urlType(self, value):
        result = True
        # Validate type merchant-urlType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 132:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_PreAuthorizedPaymentAuthCodeType(self, value):
        result = True
        # Validate type PreAuthorizedPaymentAuthCodeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PreAuthorizedPaymentAuthCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PreAuthorizedPaymentAuthCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_supplier_idType(self, value):
        result = True
        # Validate type supplier-idType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on supplier-idType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_PreAuthorizedPaymentAmountType(self, value):
        result = True
        # Validate type PreAuthorizedPaymentAmountType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on PreAuthorizedPaymentAmountType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 9999999.99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on PreAuthorizedPaymentAmountType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CurrencyType(self, value):
        result = True
        # Validate type CurrencyType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CurrencyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CurrencyType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType(self, value):
        result = True
        # Validate type transaction-typeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.merchant_name is not None or
            self.merchant_url is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.supplier_id is not None or
            self.charge_amount is not None or
            self.currency is not None or
            self.transaction_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SupplierAccountReceiptDetailsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SupplierAccountReceiptDetailsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SupplierAccountReceiptDetailsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SupplierAccountReceiptDetailsType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SupplierAccountReceiptDetailsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SupplierAccountReceiptDetailsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SupplierAccountReceiptDetailsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.merchant_name is not None:
            namespaceprefix_ = self.merchant_name_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-name>%s</%smerchant-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_name), input_name='merchant-name')), namespaceprefix_ , eol_))
        if self.merchant_url is not None:
            namespaceprefix_ = self.merchant_url_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-url>%s</%smerchant-url>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_url), input_name='merchant-url')), namespaceprefix_ , eol_))
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.supplier_id is not None:
            namespaceprefix_ = self.supplier_id_nsprefix_ + ':' if (UseCapturedNS_ and self.supplier_id_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssupplier-id>%s</%ssupplier-id>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.supplier_id), input_name='supplier-id')), namespaceprefix_ , eol_))
        if self.charge_amount is not None:
            namespaceprefix_ = self.charge_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.charge_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scharge-amount>%s</%scharge-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.charge_amount, input_name='charge-amount'), namespaceprefix_ , eol_))
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')), namespaceprefix_ , eol_))
        if self.transaction_type is not None:
            namespaceprefix_ = self.transaction_type_nsprefix_ + ':' if (UseCapturedNS_ and self.transaction_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransaction-type>%s</%stransaction-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transaction_type), input_name='transaction-type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'merchant-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_name')
            value_ = self.gds_validate_string(value_, node, 'merchant_name')
            self.merchant_name = value_
            self.merchant_name_nsprefix_ = child_.prefix
            # validate type merchant-nameType
            self.validate_merchant_nameType(self.merchant_name)
        elif nodeName_ == 'merchant-url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_url')
            value_ = self.gds_validate_string(value_, node, 'merchant_url')
            self.merchant_url = value_
            self.merchant_url_nsprefix_ = child_.prefix
            # validate type merchant-urlType
            self.validate_merchant_urlType(self.merchant_url)
        elif nodeName_ == 'auth-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'auth_code')
            value_ = self.gds_validate_string(value_, node, 'auth_code')
            self.auth_code = value_
            self.auth_code_nsprefix_ = child_.prefix
            # validate type PreAuthorizedPaymentAuthCodeType
            self.validate_PreAuthorizedPaymentAuthCodeType(self.auth_code)
        elif nodeName_ == 'auth-timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.auth_timestamp = dval_
            self.auth_timestamp_nsprefix_ = child_.prefix
        elif nodeName_ == 'supplier-id':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'supplier_id')
            value_ = self.gds_validate_string(value_, node, 'supplier_id')
            self.supplier_id = value_
            self.supplier_id_nsprefix_ = child_.prefix
            # validate type supplier-idType
            self.validate_supplier_idType(self.supplier_id)
        elif nodeName_ == 'charge-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'charge_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'charge_amount')
            self.charge_amount = fval_
            self.charge_amount_nsprefix_ = child_.prefix
            # validate type PreAuthorizedPaymentAmountType
            self.validate_PreAuthorizedPaymentAmountType(self.charge_amount)
        elif nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
            # validate type CurrencyType
            self.validate_CurrencyType(self.currency)
        elif nodeName_ == 'transaction-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transaction_type')
            value_ = self.gds_validate_string(value_, node, 'transaction_type')
            self.transaction_type = value_
            self.transaction_type_nsprefix_ = child_.prefix
            # validate type transaction-typeType
            self.validate_transaction_typeType(self.transaction_type)
# end class SupplierAccountReceiptDetailsType


class cc_receipt_details_type(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, merchant_name=None, merchant_url=None, name_on_card=None, auth_code=None, auth_timestamp=None, card_type=None, charge_amount=None, currency=None, transaction_type=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.merchant_name = merchant_name
        self.validate_merchant_nameType3(self.merchant_name)
        self.merchant_name_nsprefix_ = None
        self.merchant_url = merchant_url
        self.validate_merchant_urlType4(self.merchant_url)
        self.merchant_url_nsprefix_ = None
        self.name_on_card = name_on_card
        self.validate_CcNameType(self.name_on_card)
        self.name_on_card_nsprefix_ = None
        self.auth_code = auth_code
        self.validate_CcAuthorizationCodeType(self.auth_code)
        self.auth_code_nsprefix_ = None
        if isinstance(auth_timestamp, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(auth_timestamp, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = auth_timestamp
        self.auth_timestamp = initvalue_
        self.auth_timestamp_nsprefix_ = None
        self.card_type = card_type
        self.validate_CcType(self.card_type)
        self.card_type_nsprefix_ = None
        self.charge_amount = charge_amount
        self.validate_CcAuthorizationAmountType(self.charge_amount)
        self.charge_amount_nsprefix_ = None
        self.currency = currency
        self.validate_CurrencyType(self.currency)
        self.currency_nsprefix_ = None
        self.transaction_type = transaction_type
        self.validate_transaction_typeType5(self.transaction_type)
        self.transaction_type_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cc_receipt_details_type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cc_receipt_details_type.subclass:
            return cc_receipt_details_type.subclass(*args_, **kwargs_)
        else:
            return cc_receipt_details_type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_merchant_name(self):
        return self.merchant_name
    def set_merchant_name(self, merchant_name):
        self.merchant_name = merchant_name
    def get_merchant_url(self):
        return self.merchant_url
    def set_merchant_url(self, merchant_url):
        self.merchant_url = merchant_url
    def get_name_on_card(self):
        return self.name_on_card
    def set_name_on_card(self, name_on_card):
        self.name_on_card = name_on_card
    def get_auth_code(self):
        return self.auth_code
    def set_auth_code(self, auth_code):
        self.auth_code = auth_code
    def get_auth_timestamp(self):
        return self.auth_timestamp
    def set_auth_timestamp(self, auth_timestamp):
        self.auth_timestamp = auth_timestamp
    def get_card_type(self):
        return self.card_type
    def set_card_type(self, card_type):
        self.card_type = card_type
    def get_charge_amount(self):
        return self.charge_amount
    def set_charge_amount(self, charge_amount):
        self.charge_amount = charge_amount
    def get_currency(self):
        return self.currency
    def set_currency(self, currency):
        self.currency = currency
    def get_transaction_type(self):
        return self.transaction_type
    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type
    def validate_merchant_nameType3(self, value):
        result = True
        # Validate type merchant-nameType3, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-nameType3' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_merchant_urlType4(self, value):
        result = True
        # Validate type merchant-urlType4, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on merchant-urlType4' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CcNameType(self, value):
        result = True
        # Validate type CcNameType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CcNameType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CcNameType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_CcAuthorizationCodeType(self, value):
        result = True
        # Validate type CcAuthorizationCodeType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CcAuthorizationCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CcAuthorizationCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_CcType(self, value):
        result = True
        # Validate type CcType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CcType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_CcAuthorizationAmountType(self, value):
        result = True
        # Validate type CcAuthorizationAmountType, a restriction on xsd:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_CurrencyType(self, value):
        result = True
        # Validate type CurrencyType, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CurrencyType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CurrencyType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_transaction_typeType5(self, value):
        result = True
        # Validate type transaction-typeType5, a restriction on xsd:normalizedString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on transaction-typeType5' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def _hasContent(self):
        if (
            self.merchant_name is not None or
            self.merchant_url is not None or
            self.name_on_card is not None or
            self.auth_code is not None or
            self.auth_timestamp is not None or
            self.card_type is not None or
            self.charge_amount is not None or
            self.currency is not None or
            self.transaction_type is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-details-type', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('cc-receipt-details-type')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'cc-receipt-details-type':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='cc-receipt-details-type')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='cc-receipt-details-type', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='cc-receipt-details-type'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='cc-receipt-details-type', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.merchant_name is not None:
            namespaceprefix_ = self.merchant_name_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_name_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-name>%s</%smerchant-name>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_name), input_name='merchant-name')), namespaceprefix_ , eol_))
        if self.merchant_url is not None:
            namespaceprefix_ = self.merchant_url_nsprefix_ + ':' if (UseCapturedNS_ and self.merchant_url_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smerchant-url>%s</%smerchant-url>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.merchant_url), input_name='merchant-url')), namespaceprefix_ , eol_))
        if self.name_on_card is not None:
            namespaceprefix_ = self.name_on_card_nsprefix_ + ':' if (UseCapturedNS_ and self.name_on_card_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sname-on-card>%s</%sname-on-card>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.name_on_card), input_name='name-on-card')), namespaceprefix_ , eol_))
        if self.auth_code is not None:
            namespaceprefix_ = self.auth_code_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_code_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-code>%s</%sauth-code>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.auth_code), input_name='auth-code')), namespaceprefix_ , eol_))
        if self.auth_timestamp is not None:
            namespaceprefix_ = self.auth_timestamp_nsprefix_ + ':' if (UseCapturedNS_ and self.auth_timestamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauth-timestamp>%s</%sauth-timestamp>%s' % (namespaceprefix_ , self.gds_format_datetime(self.auth_timestamp, input_name='auth-timestamp'), namespaceprefix_ , eol_))
        if self.card_type is not None:
            namespaceprefix_ = self.card_type_nsprefix_ + ':' if (UseCapturedNS_ and self.card_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scard-type>%s</%scard-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.card_type), input_name='card-type')), namespaceprefix_ , eol_))
        if self.charge_amount is not None:
            namespaceprefix_ = self.charge_amount_nsprefix_ + ':' if (UseCapturedNS_ and self.charge_amount_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scharge-amount>%s</%scharge-amount>%s' % (namespaceprefix_ , self.gds_format_decimal(self.charge_amount, input_name='charge-amount'), namespaceprefix_ , eol_))
        if self.currency is not None:
            namespaceprefix_ = self.currency_nsprefix_ + ':' if (UseCapturedNS_ and self.currency_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scurrency>%s</%scurrency>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.currency), input_name='currency')), namespaceprefix_ , eol_))
        if self.transaction_type is not None:
            namespaceprefix_ = self.transaction_type_nsprefix_ + ':' if (UseCapturedNS_ and self.transaction_type_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransaction-type>%s</%stransaction-type>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.transaction_type), input_name='transaction-type')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'merchant-name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_name')
            value_ = self.gds_validate_string(value_, node, 'merchant_name')
            self.merchant_name = value_
            self.merchant_name_nsprefix_ = child_.prefix
            # validate type merchant-nameType3
            self.validate_merchant_nameType3(self.merchant_name)
        elif nodeName_ == 'merchant-url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'merchant_url')
            value_ = self.gds_validate_string(value_, node, 'merchant_url')
            self.merchant_url = value_
            self.merchant_url_nsprefix_ = child_.prefix
            # validate type merchant-urlType4
            self.validate_merchant_urlType4(self.merchant_url)
        elif nodeName_ == 'name-on-card':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name_on_card')
            value_ = self.gds_validate_string(value_, node, 'name_on_card')
            self.name_on_card = value_
            self.name_on_card_nsprefix_ = child_.prefix
            # validate type CcNameType
            self.validate_CcNameType(self.name_on_card)
        elif nodeName_ == 'auth-code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'auth_code')
            value_ = self.gds_validate_string(value_, node, 'auth_code')
            self.auth_code = value_
            self.auth_code_nsprefix_ = child_.prefix
            # validate type CcAuthorizationCodeType
            self.validate_CcAuthorizationCodeType(self.auth_code)
        elif nodeName_ == 'auth-timestamp':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.auth_timestamp = dval_
            self.auth_timestamp_nsprefix_ = child_.prefix
        elif nodeName_ == 'card-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'card_type')
            value_ = self.gds_validate_string(value_, node, 'card_type')
            self.card_type = value_
            self.card_type_nsprefix_ = child_.prefix
            # validate type CcType
            self.validate_CcType(self.card_type)
        elif nodeName_ == 'charge-amount' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'charge_amount')
            fval_ = self.gds_validate_decimal(fval_, node, 'charge_amount')
            self.charge_amount = fval_
            self.charge_amount_nsprefix_ = child_.prefix
            # validate type CcAuthorizationAmountType
            self.validate_CcAuthorizationAmountType(self.charge_amount)
        elif nodeName_ == 'currency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currency')
            value_ = self.gds_validate_string(value_, node, 'currency')
            self.currency = value_
            self.currency_nsprefix_ = child_.prefix
            # validate type CurrencyType
            self.validate_CurrencyType(self.currency)
        elif nodeName_ == 'transaction-type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'transaction_type')
            value_ = self.gds_validate_string(value_, node, 'transaction_type')
            self.transaction_type = value_
            self.transaction_type_nsprefix_ = child_.prefix
            # validate type transaction-typeType5
            self.validate_transaction_typeType5(self.transaction_type)
# end class cc_receipt_details_type


class linksType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if link is None:
            self.link = []
        else:
            self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, linksType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if linksType.subclass:
            return linksType.subclass(*args_, **kwargs_)
        else:
            return linksType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def add_link(self, value):
        self.link.append(value)
    def insert_link_at(self, index, value):
        self.link.insert(index, value)
    def replace_link_at(self, index, value):
        self.link[index] = value
    def _hasContent(self):
        if (
            self.link
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='linksType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('linksType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'linksType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='linksType')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='linksType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='linksType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='linksType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for link_ in self.link:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            link_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='link', pretty_print=pretty_print)
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
        if nodeName_ == 'link':
            obj_ = LinkType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.link.append(obj_)
            obj_.original_tagname_ = 'link'
# end class linksType


class linksType1(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, link=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if link is None:
            self.link = []
        else:
            self.link = link
        self.link_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, linksType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if linksType1.subclass:
            return linksType1.subclass(*args_, **kwargs_)
        else:
            return linksType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_link(self):
        return self.link
    def set_link(self, link):
        self.link = link
    def add_link(self, value):
        self.link.append(value)
    def insert_link_at(self, index, value):
        self.link.insert(index, value)
    def replace_link_at(self, index, value):
        self.link[index] = value
    def _hasContent(self):
        if (
            self.link
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='linksType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('linksType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'linksType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='linksType1')
        if self._hasContent():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='linksType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='linksType1'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='linksType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for link_ in self.link:
            namespaceprefix_ = self.link_nsprefix_ + ':' if (UseCapturedNS_ and self.link_nsprefix_) else ''
            link_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='link', pretty_print=pretty_print)
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
        if nodeName_ == 'link':
            obj_ = LinkType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.link.append(obj_)
            obj_.original_tagname_ = 'link'
# end class linksType1


GDSClassesMapping = {
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
        rootTag = 'PickupRequestDetailsType'
        rootClass = PickupRequestDetailsType
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
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PickupRequestDetailsType'
        rootClass = PickupRequestDetailsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
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
    return rootObj, rootElement, mapping, reverse_mapping


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
        rootTag = 'PickupRequestDetailsType'
        rootClass = PickupRequestDetailsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
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
        rootTag = 'PickupRequestDetailsType'
        rootClass = PickupRequestDetailsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from pickuprequest import *\n\n')
        sys.stdout.write('import pickuprequest as model_\n\n')
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
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.canadapost.ca/ws/pickuprequest': [('PickupTypeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PreAuthorizedPaymentAccountNumberType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PreAuthorizedPaymentAuthCodeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PreAuthorizedPaymentAmountType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('DayOfTheWeekType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PickupTimeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('RelType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PostalCodeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('ProvinceType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('EmailType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PhoneType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PhoneExtentionType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CustomerRequestIDType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('ContractIDType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('MethodOfPaymentType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('RequestIDType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PickupVolumeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PickupStatusType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CostTypeNonZero',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CostTypeAllowsZero',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CostTypeAllowsNegative',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CcType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CcMaskedNumberType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CcNameType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CcAuthorizationCodeType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CcAuthorizationAmountType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('CurrencyType',
                                                './schemas/pickuprequest.xsd',
                                                'ST'),
                                               ('PickupRequestDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestUpdateDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestDetailedInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestResponseDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('HoldPickupsInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ResumePickupsInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupLocationType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('AlternateAddressType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ContactInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ContactInfoResponseDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('LocationDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ItemsCharacteristicsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ItemsCharacteristicsUpdateDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupTimesType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('OnDemandPickupTimeType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('ScheduledPickupTimesType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupTimesPerDayType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PaymentInfoType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PreAuthorizedPaymentType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestHeaderType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('LinkType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestPriceType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('PickupRequestPriceNoCCType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('SupplierAccountReceiptDetailsType',
                                                './schemas/pickuprequest.xsd',
                                                'CT'),
                                               ('cc_receipt_details_type',
                                                './schemas/pickuprequest.xsd',
                                                'CT')]}

__all__ = [
    "AlternateAddressType",
    "ContactInfoResponseDetailsType",
    "ContactInfoType",
    "HoldPickupsInfoType",
    "ItemsCharacteristicsType",
    "ItemsCharacteristicsUpdateDetailsType",
    "LinkType",
    "LocationDetailsType",
    "OnDemandPickupTimeType",
    "PaymentInfoType",
    "PickupDetailsType",
    "PickupLocationType",
    "PickupRequestDetailedInfoType",
    "PickupRequestDetailsType",
    "PickupRequestHeaderType",
    "PickupRequestInfoType",
    "PickupRequestPriceNoCCType",
    "PickupRequestPriceType",
    "PickupRequestResponseDetailsType",
    "PickupRequestType",
    "PickupRequestUpdateDetailsType",
    "PickupRequestsType",
    "PickupTimesPerDayType",
    "PickupTimesType",
    "PreAuthorizedPaymentType",
    "ResumePickupsInfoType",
    "ScheduledPickupTimesType",
    "SupplierAccountReceiptDetailsType",
    "cc_receipt_details_type",
    "linksType",
    "linksType1"
]
