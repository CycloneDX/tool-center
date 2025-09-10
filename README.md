# CycloneDX Tool Center

The CycloneDX Tool Center is the largest publicly available collection of SBOM (Software Bill of Materials) and xBOM (e.g., SaaSBOM, CBOM, HBOM) products, projects, and services. It serves as a centralized resource for anyone looking to explore, evaluate, or integrate BOM-related capabilities into their toolchains and workflows. The Tool Center is an integral part of the [CycloneDX website](https://cyclonedx.org).

As of March 2025, the CycloneDX Tool Center leverages a JSON Schema in which `tools.json` must validate against. [View the human-readable documentation for the JSON Schema](https://cyclonedx.github.io/tool-center/).  
As of September 2025, the `tools.json` is assembled automatically from the individual JSON files in the `tools/` folder. Do not modify `tools.json` directly, instead add/modify individual files in the `tools/`folder.

## License

All data within this repository is provided under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) license. You are free to use, modify, and redistribute the data in accordance with the terms of this license.

## Contributing

Contributions are welcome! If you know of a tool, product, or service related to SBOM or xBOM (SaaSBOM, CBOM, HBOM) that isn’t listed, please feel free to open a pull request or file an issue. When contributing, ensure that:

- The tool is relevant to SBOM/xBOM generation, analysis, or consumption.
- Any provided metadata or descriptions are accurate and up-to-date.
- Licensing and attribution requirements for tools are respected.

Creating/editing a file in the `tools/` folder manually can be complicated. An alternative is to use
[MetaConfigurator](https://www.metaconfigurator.org?schema=https://raw.githubusercontent.com/CycloneDX/tool-center/refs/heads/main/schemas/tool.schema.json&settings=https://raw.githubusercontent.com/CycloneDX/tool-center/refs/heads/main/metaConfiguratorSettings.json) to make changes then download the edited data.

## Community & Support

If you have questions, suggestions, or feedback about the CycloneDX Tool Center, we encourage you to:

- Join the [CycloneDX Slack](https://cyclonedx.org/slack) ([invite](https://cyclonedx.org/slack/invite)) for real-time discussions.
- Visit the [CycloneDX website](https://cyclonedx.org) for documentation, news, and updates.
- Open an issue in this repository for any corrections or clarifications.

By leveraging the Tool Center’s data, users and organizations can more easily discover solutions, accelerate their SBOM and xBOM adoption, and enhance the security and transparency of their software supply chains.
