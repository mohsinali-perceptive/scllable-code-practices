def transform_to_xml(payload):
    return """<?xml version="1.0" encoding="utf-8"?>
    <root>
        <employee>
            <name>Alice</name>
            <role>Developer</role>
            <skills>
                <item>Python</item>
                <item>SQL</item>
            </skills>
        </employee>
    </root>
    """