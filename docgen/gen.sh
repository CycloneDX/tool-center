#!/bin/bash
set -eu

# Description
DESC="Generate HTML Schema navigator for CycloneDX Tool Center"

# Paths (adjust if needed)
THIS_PATH="$(realpath "$(dirname "$0")")"
SCHEMA_PATH="$(realpath "$THIS_PATH/../schemas")"
DOCS_PATH="$THIS_PATH/docs"
TEMPLATES_PATH="$THIS_PATH/templates"

prepare () {
  # Check if generate-schema-doc is installed
  if ! command -v generate-schema-doc > /dev/null 2>&1; then
    # Install dependencies from local requirements.txt
    python -m pip install -r "$THIS_PATH/requirements.txt"
  fi
}

clean () {
  rm -rf "$DOCS_PATH"
  mkdir -p "$DOCS_PATH"
}

_generate () {
  local title="$1"
  local schema_file="$2"
  local out_file="$3"

  # Generate HTML documentation from the JSON schema
  generate-schema-doc \
    --config no_link_to_reused_ref \
    --config no_show_breadcrumbs \
    --config no_collapse_long_descriptions \
    --deprecated-from-description \
    --config title="$title" \
    --config custom_template_path="$TEMPLATES_PATH/cyclonedx/base.html" \
    --minify \
    "$schema_file" \
    "$out_file"

  # Update placeholders in the generated HTML
  sed -i -e "s/\${quotedTitle}/\"$title\"/g" "$out_file"
  sed -i -e "s/\${title}/$title/g" "$out_file"
}


generate_tools () {
  _generate \
  "CycloneDX Tool Center v2 - Tools - JSON Reference"\
  "$SCHEMA_PATH/tools.schema.json" \
  "$DOCS_PATH/index.html"
}

generate_tool () {
  _generate \
  "CycloneDX Tool Center v2 - Tool - JSON Reference"\
  "$SCHEMA_PATH/tool.schema.json" \
  "$DOCS_PATH/tool.html"
}

# Main
prepare
clean
generate_tools
generate_tool

exit 0
