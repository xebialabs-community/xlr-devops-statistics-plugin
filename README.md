
# DevOps Statistics Integration for XL Release

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-devops-statistics-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-devops-statistics-plugin)
![GitHub release](https://img.shields.io/github/release/xebialabs-community/xlr-devops-statistics-plugin.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Github All Releases](https://img.shields.io/github/downloads/xebialabs-community/xlr-devops-statistics-plugin/total.svg)](https://github.com/xebialabs-community/xlr-devops-statistics-plugin/releases)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-blue.svg)](https://github.com/RichardLitt/standard-readme)

## Installation

### Requirements

1. XL Release 9.0+

### Building the plugin
The gradle wrapper facilitates building the plugin.  Use the following command to build using [Gradle](https://gradle.org/):
```bash
./gradlew clean build
```
The built plugin, along with other files from the build, can then be found in the _build_ folder.

### Adding the plugin to XL Release

Download the latest version of the plugin from the [releases page](https://github.com/xebialabs-community/xlr-devops-statistics-plugin/releases).  The plugin can then be installed through the XL Release graphical interface or the server backend.  For additional detail, please refer to [the docs.xebialabs.com documentation on XLR plugin installation](https://docs.xebialabs.com/xl-release/how-to/install-or-remove-xl-release-plugins.html)

## Usage

__Available Tasks__: None

__Available Triggers__: None

__Available Dashboard Tiles__: Delivery Size Tile, Task Metrics Tile

### Tiles

#### Delivery Size Tile
Properties:
* Title  
   * Tile title
* Delivery Scope _input_ 
   * Include deliveries that are progress, completed, or all (both).
* Max Count _input_ 
   * How many of the latest deliveries to show in the dashboard tile.
* Latest _input_ 
   * Which datetime should be used when gathering the latest deliveries.

#### Task Metrics Tile
Properties:
* Title  
   * Tile title
* From Datetime _input_ 
   * Filter to only include tasks executed after this datetime
* To Datetime _input_ 
   * Filter to only include tasks executed before this datetime
* Date Aggregation _input_ 
   * A time period for aggregation.  This value determines how granular the date axis is.
* Release Tags _input_ 
   * Only include releases which have one of these tags
* Task Tags _input_ 
   * Only include release tasks which have one of these tags

## Contributing

Please review the contributing guidelines for _xebialabs-community_ at [http://xebialabs-community.github.io/](http://xebialabs-community.github.io/)

## License

This community plugin is licensed under the [MIT license](https://opensource.org/licenses/MIT).

See license in [LICENSE.md](LICENSE.md)
