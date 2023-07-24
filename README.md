# 基于Flask的问答平台系统的设计与实现

[github地址：https://github.com/XcNgg/question_project/tree/master](https://github.com/XcNgg/question_project/tree/master)

**摘 要：** 随着互联网技术的快速发展，问答平台系统已经成为了一种非常流行的网络应用平台。本文针对写问答平台系统进行研究和开发，提供一个高效、实用、易用的问答平台，为用户提供优质的知识交流和分享服务。

本文介绍了基于Flask的问答平台系统的基本概念、特点和发展历程。然后，基于用户需求和功能需求，提出并设计了一个基于Web的写问答平台系统的架构。系统通过SQLAlchemy实现ORM的数据模型架构，前端采用Bootstrap框架实现响应式布局，后端使用Flask框架和MySQL数据库实现数据管理和交互。系统主要包括用户管理、问答管理、评论管理和站内信管理等功能。用户可以通过注册登录账号、搜索问答内容、发布问题和回答问题等操作参与问答平台的互动交流。

本文的贡献在于提出并实现了一个基于Web的写问答平台系统，为用户提供了一个有效的知识交流和分享平台。同时，本文的研究和设计实践也为问答平台系统的发展提供了一些借鉴意义。

**关键词** ： Flask；Web应用开发；MySQL；

# 1 绪论

## 1.1研究背景及意义

进入新世纪以来，随着国家的综合实力的提升，人们物质文化生活水平的提升，新一代的互联网用户开始不再满足于互联网所带来的娱乐功能，开始利用触手可及的互联网平台获取广袤的知识来满足自己的好奇心。对未知的事物与知识的渴求与探索是人类发展过程中一直存在的现象，倡导分享与开放的互联网为此提供了一个最好的媒介。但是由于很多人受限于自身影响力以及产品号召力，缺乏相应的平台和培训指导，缺少相应的相互交流和学习的平台，导致资源的配置效率并不高，在没有相应的人力和财力的在宣传上，很多创意都只能是纸上谈兵，没有机会经历市场和社会的检验。因此用户需要一种平台，汲取不同的知识，并与同样渴望知识的用户进行沟通与互动。作为寻求答案的优先途径，在线问答社区网站这种新式社交平台，开始扮演了一个独具特色的信息沟通方式的角色。

问答平台的出现缩小了用户与知识之间的距离，它将来自全球的不同的用户聚集在一起，成为人们获取咨询、解决问题以及分享知识的重要途径。其管理和维护问题、答案的机制以及问答交互中的语言带来了大量的研究问题，并促进了问答平台的理论和实践研究。在当今的互联网中，国内外著名的Quora、Stack Overflow、知乎等优秀的问答社交平台慢慢的成为了广大用户学习知识、分享新兴事物、满好奇心、与经验的重要途径。这类互联网平台的发展蕴示着人们获取知识的途径越来越多的依托互联网平台。

## 1.2论文的主要研究内容

论文主要实现了基于Flask的问答平台系统，平台允许用户在自己的注册账号，登录平台，可在平台内发布问题、回复其他用户发表的问题，同时用户也可以发布自己在生活、工作、学习中遇到的事情的经验分享。为了良好的用户体验，同时平台还有搜索功能，帮助用户更为便捷搜索到自己所需的问题内容。论文主要包含三个部分:

1. 第一章绪论，该部分首先介绍了基于 Flask 的知识问答平台的研究背景。
2. 第二章项目技术与研究，介绍了系统实现的主要技术，包括Bootstrap框架、Flask框架，Ajax 技术、JavaScript库jQuery、MySQL数据库，ORM数据模型。
3. 第三章问答系统设计与实现，该部分主要分为两部分，首先是对问答平台的系统配置、用户管理设计等。然后是平台各模块详细的实现过程。

# 2 项目技术与研究

## 2.1 响应式布局Bootstrap

本项目中，使用的Bootstrap version 4.6.1版本，主要用于完成项目的前端页面开发，以及多终端，多设备中的响应式交互。

Bootstrap是一个流行的前端开发框架，由Twitter公司的开发团队在2010年推出。它基于HTML、CSS和JavaScript，并提供了许多预先定义的组件和样式，可以帮助开发人员快速构建响应式的网站和应用程序。

下面详细介绍Bootstrap的几个方面：

- 栅格系统（Grid System）：Bootstrap的栅格系统是一种用于布局的工具，它将屏幕分成12个等宽的列，开发人员可以使用这些列来创建灵活的布局，以适应不同大小的设备。栅格系统可以在HTML中使用class属性来指定，例如col-sm-6表示在小屏幕设备上该元素占据6列。
- 预定义的组件（Predefined Components）：Bootstrap提供了许多预定义的组件，例如导航栏、表格、表单、按钮、标签等等。这些组件具有一致的样式和行为，可以减少开发人员的工作量，同时确保整个应用程序的外观和行为一致。
- 响应式设计（Responsive Design）：Bootstrap支持响应式设计，可以自适应不同的设备尺寸，例如桌面、平板电脑和手机等。开发人员可以使用Bootstrap提供的类来控制不同设备上元素的显示和隐藏，以确保在不同的设备上都能够良好地展示。
- JavaScript插件（JavaScript Plugins）：Bootstrap提供了许多JavaScript插件，例如模态框、轮播图、滚动条等等。这些插件可以在网页中轻松地引入和使用，同时也具有一致的样式和行为。

综上所述，Bootstrap是一个功能强大的前端开发框架，可以帮助开发人员快速构建响应式的网站和应用程序。它的栅格系统、预定义的组件、响应式设计和JavaScript插件等功能，可以帮助开发人员节省时间和精力，同时确保应用程序具有一致的外观和行为。

## 2.2 异步更新 Ajax 技术

在本项目中，使用到了jQuery实现Ajax技术。

异步更新是一种Web开发技术，用于在不刷新整个页面的情况下更新Web页面的一部分。其中，Ajax（Asynchronous JavaScript and XML）是异步更新的一种实现方式，它可以通过JavaScript向服务器发送HTTP请求，获取数据并更新Web页面上的一部分内容。

传统的Web页面更新方式是同步更新，即用户操作后，服务器会重新加载整个页面并返回更新后的页面，这种方式的缺点是会导致页面的反应速度较慢，用户体验差。而异步更新可以只更新页面上的部分内容，避免重新加载整个页面，从而提高页面的响应速度和用户体验。

Ajax技术实现异步更新的过程如下：

1. 用户操作触发JavaScript代码执行。
2. JavaScript代码通过XMLHttpRequest对象向服务器发送HTTP请求。
3. 服务器处理请求，返回相应的数据。
4. JavaScript代码解析服务器返回的数据，并更新Web页面上的对应部分。

由于Ajax是异步更新的一种实现方式，它可以在不阻塞其他JavaScript代码执行的情况下，向服务器发送请求并处理返回的数据。这使得Web应用程序可以在后台获取数据并更新页面，而无需用户手动刷新整个页面。Ajax还可以在数据传输的过程中提供一些用户体验上的改进，例如显示进度条或加载动画等。

综上所述，Ajax是一种实现异步更新的Web开发技术，通过JavaScript向服务器发送HTTP请求，获取数据并更新Web页面上的一部分内容，从而提高页面的响应速度和用户体验。

## 2.3 跨浏览器JavaScript库jQuery

在本项目中，使用到了jQuery version 3.6.0版本，主要用于实现前端开发与异步交互技术。

jQuery是一个流行的JavaScript库，它是用于简化JavaScript代码的编写和操作DOM元素的一种工具，由John Resig于2006年创建。jQuery在网页开发中得到了广泛的应用，因为它可以使开发人员更快速、更方便地操作Web页面，同时解决了浏览器兼容性问题。

下面是jQuery的一些主要特点：

- 简化DOM操作：jQuery提供了简单而强大的DOM操作方法，可以使用更少的代码来完成各种操作，例如查找元素、修改元素属性、添加/删除元素等等。
- 事件处理：jQuery可以轻松地处理事件，例如鼠标单击、鼠标悬停、键盘敲击等等，同时还可以处理事件的冒泡和委托。
- AJAX支持：jQuery提供了简化AJAX的方法，可以轻松地向服务器发送HTTP请求，处理响应并更新Web页面上的内容。
- 动画效果：jQuery提供了多种动画效果，可以轻松地添加动画效果，例如淡入淡出、滑动、缩放等等，同时还可以自定义动画效果。
- 插件支持：jQuery的插件支持非常好，可以在不修改核心代码的情况下扩展jQuery的功能。

综上所述，jQuery是一个简单而强大的JavaScript库，它可以使开发人员更快速、更方便地操作Web页面，解决浏览器兼容性问题，并提供了丰富的功能和插件支持。由于jQuery的流行，现在许多网站都使用jQuery来简化JavaScript代码的编写，提高Web开发效率。

## 2.4 轻量级可制定Flask框架

在本项目中，Flask框架主要用于网页后端的构建。

Flask是一个Python Web框架，它是一个轻量级的框架，具有灵活性和可扩展性。Flask提供了一组简单而有用的工具，可以帮助开发人员快速构建Web应用程序。与其他Web框架相比，Flask的学习曲线相对较低，因此非常适合初学者。

以下是Flask的一些主要特点：

- 轻量级框架：Flask非常轻量，没有复杂的配置和大量的依赖，这使得它易于学习和使用。
- 易于扩展：Flask的设计使得它非常容易扩展，可以通过使用扩展包来添加功能，例如ORM（对象关系映射）库、表单验证、身份验证等等。
- 灵活性：Flask提供了非常灵活的URL路由，可以轻松地处理不同类型的请求，例如GET、POST等等。同时，Flask还可以通过Jinja2模板引擎提供动态Web内容。
- 兼容性：Flask与许多其他Python库和工具兼容，包括SQLAlchemy、WTForms、Celery等等。
- 安全性：Flask提供了安全性的保护，例如CSRF（跨站请求伪造）保护和XSS（跨站脚本攻击）保护。

在本项目中，也包括了使用Jinjia2、蓝图视图、Flask-wtf、Flask-Migrate等多功能Python库或扩展插件，以实现网站正常运行。其中重点使用了Jinjia2用于网页前后端交互的动态渲染，Jinja2是一个流行的Python模板引擎，用于生成动态HTML网页和其他文本格式。它是Flask Web框架的默认模板引擎，也可用于其他Python Web框架和应用程序。具有语法简单、模板继承、自定义过滤器、变量转义防止XSS攻击等特点。

综上所述，Flask是一个灵活、易于学习和使用的Python Web框架，适合用于构建小型Web应用程序和API。Flask通过提供简单但有用的工具来帮助开发人员快速构建Web应用程序，同时它的灵活性和可扩展性可以满足各种不同的需求。

## 2.5 数据持久化MySQL数据库

MySQL是一种开源的关系型数据库管理系统（RDBMS），最初由瑞典MySQL AB公司开发。它是一种高效、可靠、易于使用的数据库系统，广泛用于Web应用程序、企业应用程序、数据仓库、嵌入式系统等领域。它提供了一种可靠的方式来存储和管理数据。数据持久化是指将数据存储到磁盘或其他非易失性存储介质中，以确保在计算机系统关闭或出现故障时，数据仍然能够被恢复和访问。

MySQL的数据持久化机制保证了数据的可靠性和完整性，即使在系统崩溃或断电时，也能够保证数据不会丢失。这对于许多应用程序来说是非常重要的，特别是对于金融、电子商务、医疗保健等领域的应用程序。

MySQL提供了广泛的功能和工具，包括事务处理、复制、高可用性、安全性、数据备份和恢复等。在MySQL中，数据持久化通常通过将数据写入磁盘上的文件来实现。MySQL将所有数据存储在磁盘上的文件中，这些文件包括数据表、索引、日志文件等。在MySQL中，可以使用不同的存储引擎来实现数据持久化，包括InnoDB、MyISAM、Memory等，每种存储引擎都有其独特的特性和优缺点，可以根据具体的应用场景来选择不同的存储引擎。

MySQL的核心功能是SQL（Structured Query Language）查询语言，它允许用户通过编写SQL语句来查询和操作数据库中的数据。MySQL支持标准的SQL语法，同时也支持一些扩展语法，例如存储过程、触发器等。MySQL还支持索引、视图、存储过程、触发器等高级特性，可以满足各种复杂的数据处理需求。

MySQL具有以下特点：

- 开源：MySQL是一种开源软件，其源代码可以自由地下载、使用和修改，这使得它成为了许多开发者和组织的首选数据库系统。
- 可靠性：MySQL具有高可靠性，它支持数据持久化机制，保证了数据的完整性和可靠性，即使在系统崩溃或断电时，也能够保证数据不会丢失。
- 高效性：MySQL是一种高效的数据库系统，它具有高速读写能力、支持高并发访问和高性能的查询处理。
- 安全性：MySQL提供了多种安全功能，包括访问控制、数据加密和身份验证等，以保护数据不被非法访问和窃取。

综上所述，MySQL是一个稳定、可靠和高效的数据库管理系统，被广泛应用于各种类型的应用程序，包括Web应用程序、企业应用程序、移动应用程序等。MySQL的开源性质和庞大的社区支持，也使得它成为了一个受欢迎的数据库选择。

## 2.6 ORM数据模型SQLAlchemy

本项目使用Python库SQLAlchemy来管理ORM数据模型，并除此之外，为了项目数据库的迁移便捷性，本项目还使用了Flask-Migrate，通过简单的命令行来完成数据库的快速部署迁移。

ORM（Object-Relational Mapping）是一种将面向对象编程语言中的对象与关系型数据库之间进行映射的技术。ORM可以将对象表示为数据库中的表和列，同时也可以将数据库中的表和列表示为对象。ORM可以让开发人员使用面向对象的方式来操作数据库，而不必直接编写SQL语句。

SQLAlchemy是一个Python编程语言中广受欢迎的ORM框架。它提供了一种基于Python语言的面向对象的接口，用于管理关系型数据库中的数据。SQLAlchemy的核心特性包括ORM、连接池、事务、SQL表达式和查询构建器等。SQLAlchemy的ORM组件可以自动生成SQL语句，从而实现面向对象和关系型数据库之间的映射。

SQLAlchemy的ORM组件提供了多种映射关系，包括一对一、一对多、多对多等，可以用于管理复杂的数据模型。SQLAlchemy的ORM组件还提供了事务管理、延迟加载、缓存等功能，可以提高应用程序的性能和可维护性。同时，SQLAlchemy还提供了对多种关系型数据库的支持，例如MySQL、PostgreSQL、SQLite等。

使用SQLAlchemy可以大大简化应用程序与数据库之间的交互，同时也可以提高代码的可读性和可维护性。ORM将数据库表映射为Python类，使得开发人员可以通过面向对象的方式来操作数据库，而不必直接编写SQL语句。此外，ORM还提供了许多高级功能，例如事务处理、延迟加载、缓存等，可以帮助开发人员更加轻松地管理和操作数据库。

# 3 问答系统设计与实现

## 3.1 问答系统配置

### 3.1.1 Flask文件目录管理

![image-20230724205539049.png][1]

本项目全部文件结构如图所示，最外层的Python代码分别是：

- py：主要用于配置Flask应用项目与应用项目插件初始化等信息。
- py：主要用于配置数据库的连接，邮件发送stmp协议配置信息等。
- py： 主要用于配置全局装饰器，其中包括限制只有登录了才能访问的装饰器。
- py：主要用于ORM模型配置数据库模型与验证，其中包括emial验证码模型、用户信息存储模型、发布问答的模型等。
- project\_extension.py：主要用于配置项目的扩展插件，其中包括Flask\_sqlalchemy、Flask\_mail等。

![image-20230724205558895.png][2]

如图，在static与templates目录下均是前端代码，其中包含bootstrap4.6.1、jquery3.6.0、popper等前端框架，而后是templates目录下的网页html模板代码，包括base.html网页全局模板代码、login.html登录界面、regist.html注册界面、STMP邮件验证码模板emialbase.html、question\_public.html发布问答界面、评论detial.html等。

![image-20230724205605557.png][3]

在使用Flask-Migrate进行数据库迁移时，会自动生成一个名为migrations的目录，用于存储版本信息和迁移脚本。migrations目录中包含多个文件和文件夹，每个文件和文件夹都有特定的作用。下面逐一介绍migrations目录中的文件和文件夹：

- ini：与Alembic相关的配置文件，包括数据库连接等设置。
- py：与Alembic相关的Python模块，用于生成迁移脚本和操作数据库。
- README：说明文件，描述了migrations目录的生成、作用和处理。
- py.mako：模板文件，在生成迁移脚本之间被插值。
- versions：存储数据库迁移脚本的文件夹，每个迁移脚本都是一个Python脚本，其中包含了操作数据库的Python代码。

其中，versions目录是最为重要的部分，它存储了所有的数据库迁移脚本，每个迁移脚本包含两：upgrade()和downgrade()。其中，upgrade()函数用于将数据库升级到新版本，而downgrade()函数则用于将数据库降级回旧版本。

通过执行flask db migrate命令，Flask-Migrate将检测数据库模型的变化，并创建新的迁移脚本，并将其保存到migrations目录中的versions子目录中。在此过程中，Flask-Migrate还将向alembic\_version表中添加一行数据，表明当前是哪个版本。

再通过执行flask db upgrade命令，Flask-Migrate将会将数据库转换为最新的版本，即应用由flask db migrate生成的所有尚未应用的迁移脚本。例如，在升级时Flask-Migrate会在versions目录中按照设定的顺序载入并执行每个迁移脚本的upgrade()函数，将数据库逐步迁移到新的版本。

### 3.1.2 Flask 蓝图设计

Blueprints蓝图设计是Flask中用于创建可重用功能组件的一种方式，它允许将应用程序分解为独立的模块，并使其可以轻松地实现在不同应用程序甚至不同项目中的重用。

Blueprints提供了一种将路由、模板、静态文件等组织在一起的方式，并使其能够以独立于应用程序的方式进行配置和注册。具体地说，Blueprints提供了如下的几个优点：

- 分离和组织代码逻辑：将应用程序的代码逻辑分离为与路由相关的蓝图、数据相关的模型、视图和业务逻辑相关的服务层等。
- 代码的可重用性：可以将蓝图作为一个独立的模块，供多个应用程序或项目重用。
- 避免模板、路由冲突：当多个应用程序（例如在多个应用程序中选择部分）具有相同的路由或模板名称时，蓝图可以有效避免路由、模板等资源的命名冲突。
- 简化应用程序配置：可以将蓝图的应用程序配置专用于蓝图，使应用程序配置文件变得更简单。

使用Flask Blueprint时，通常需要在蓝图中作如下配置：

1. 定义蓝图：通过Blueprint类定义蓝图，可以在需要时为其提供名称和URL前缀等相关信息。
2. 配置蓝图：针对蓝图定义路由、模板、静态文件等内容。
3. 注册蓝图：在Flask应用中注册蓝图，可以使用register\_blueprint()函数注册在应用中。

![image-20230724205613951.png][4]

如图，该应用程序仅在主应用程序中定义了两个路由，并在"/login"与"/logout"上公开它们。这种方式使用单一文件组织代码，并且很容易实现，但随着代码的增长，它的可维护性会变得更差。

![image-20230724205623164.png][5]

以上代码中，Blueprint()函数用于创建一个名为user的蓝图，两个@user\_bp.route()装饰器定义了两个路由规则。最后，使用register\_blueprint()函数将蓝图注册到Flask应用中并指定了URL前缀为"/user/"。该应用程序在"/user/"上公开了两个简单的路由，通过Blueprint注册到主应用程序中。这使得应用程序更加模块化，并且在添加更多功能时更加方便。

使用Blueprints蓝图可以使应用程序的代码更加结构化和清晰，使得在多人协作的情况下更容易维护和管理。同时，也方便了代码的重用和可扩展性的实现。

![image-20230724205629178.png][6]

如图，在本项目目录中的\_\_pycache\_\_用于存储Python解释器编译Python代码的缓存文件。Python解释器在执行代码之前，将源代码编译为字节码，以便在稍后再次引用该代码时，可以更快地加载和执行。这样可以避免每次执行代码时都要重新解析和编译代码的性能损失。在Python 3.2及以上版本中，Python解释器会在每个包含Python模块的目录下创建一个\_\_pycache\_\_目录，并在其中存储由相应的Python模块编译生成的缓存文件。这些缓存文件的文件名是基于Python模块名称和Python解释器版本号计算出来的，并以.pyc文件扩展名结尾。\_\_pycache\_\_目录可以在需要时自动生成和更新，也可以手动删除以清除缓存文件。通常情况下，不需要手动管理\_\_pycache\_\_目录，因为Python解释器会自动处理这些缓存文件，并在需要时快速加载和执行Python代码。

目录中的\_\_init\_\_.py是Python包的一个特殊文件，用于指示Python解释器该目录是一个包，并定义该包的内容。具体来说，\_\_init\_\_.py的作用有以下几点：

- 将目录转化为Python包：当Python解释器遇到一个目录时，如果它包含一个\_\_init\_\_.py文件，那么它就将该目录视为Python包。否则，它将只将该目录视为普通目录。
- 定义包级别变量和函数：在\_\_init\_\_.py文件中，可以定义与包相关的全局变量、函数和类。这些变量、函数和类将成为该包的公共API，可以被其他模块通过import语句进行访问。
- 控制模块导入行为：如果\_\_init\_\_.py文件是空的，那么该包的默认导入行为将是导入该包所包含的所有模块。但是，可以通过在init文件中定义all变量来显式指定导入的模块列表。此外，还可以在init.py`中处理模块导入的异常和错误。

综上所述，\_\_init\_\_.py文件是用于定义Python包的内容和行为的重要文件。它使得我们可以组织和管理多个模块，并提供统一的公共API进行访问和导入。

其次是the\_users.py、question.py、project\_forms.py三个Python文件。

- project\_forms.py：主要用于验证用户注册、登录以及发布问题、评论是否符合相应的规则。
- py: 问答系统的首页蓝图管理，注册路由为"/"。
- the\_users.py：问答系统的用户蓝图管理，注册路由为"/users"。

### 3.1.3 问答系统配置文件

![image-20230724205636126.png][7]

图3.7 配置文件指定

在app.py文件中，指定了Flask问答系统的配置文件。

![image-20230724205649108.png][8]

如图，该部分为数据库与SQLAlchemy等相关配置，主要用于系统的数据库连接与相关数据模型处理。

![image-20230724205658679.png][9]

在Flask应用程序中，SECRET\_KEY是一个配置变量，用于提供一个加密密钥，以确保所有传输的数据的完整性和安全性。具体来说，SECRET\_KEY的作用有以下三个方面：

- 保护用户会话：在Flask应用程序中，用户会话是指存储在客户端和服务器之间的数据，用于标识和跟踪用户的活动和状态。如果未加密这些会话数据，攻击者可以轻松地窃取用户的身份和敏感信息。通过设置SECRET\_KEY，Flask应用程序可以使用这个密钥加密和解密会话数据，确保会话安全性。
- 支持表单验证：在Flask应用程序中，表单验证是指对用户提交的表单数据进行验证，以确保数据的有效性和完整性。通过设置SECRET\_KEY，Flask可以对表单数据进行加密和解密，并使用该密钥保护表单数据的安全性。
- 实现加密功能：在某些情况下，Flask应用程序可能需要将某些数据加密，以防止数据泄露或被篡改。通过设置SECRET\_KEY，Flask可以使用该密钥对数据进行加密和解密，并保证数据的完整性和安全性。

因此，SECRET\_KEY是一个非常重要的配置变量，在Flask应用程序中确保数据的安全性和完整性。建议将其设置为一个随机字符串，足够长且足够复杂，以确保安全性。

![image-20230724205706597.png][10]

由于用户会使用到邮件注册功能，因此使用到了Flask-email的插件，该插件可以使用基于smtp的邮件传输协议，发送验证码给注册的用户。

![image-20230724205714565.png][11]

其中MAIL\_SERVER与MAIL\_PORT为提供smtp的QQ邮箱服务器，是默认不变的，重点在于MAIL\_USERNAME、MAIL\_PASSWORD，他们分别指的是发送邮箱用户的邮箱以及smtp邮件的密钥，这需要在QQ邮箱中手动开启smtp服务，获取密钥。

## 3.2 用户管理

在用户模块，主要实现邮箱注册，邮箱验证码验证过期、用户登录等。

### 3.2.1 用户注册

![image-20230724205722399.png][12]

在用户注册模块，使用Blueprint类创建蓝图对象，命名为users，并设置其URL前缀为/users。这里的\_\_name\_\_参数表示当前模块的名称。

在users蓝图中定义一个/regist路由，用于处理注册的GET和POST请求。

当接收到GET请求时，返回渲染regist.html模板的响应。

![image-20230724205729816.png][13]

如果得到的是POST请求，则需要通过form = RegistForm(request.form)获取表单数据实例化，其中，RegistForm是从project\_forms.py导入的，并调用form.validate()方法进行表单验证。

![image-20230724205729816.png][14]

如果验证通过，获取表单数据并将其实例化存储到users\_information用户信息模型数据模型中，其中密码使用generate\_password\_hash函数进行哈希存储。然后，将user\_info记录添加到数据库会话中，以便将其插入到数据库表中，完成上述操作后，将页面重定向到登录界面。

如果验证不通过，重定向到注册界面，让用户重新填写。

![image-20230724205741426.png][15]
![image-20230724205748163.png][16]

如图，上述代码均为regist.html的前端HTML代码，通过{% extends "base.html" %}Jinjia2的语法，regist.html继承了base.html的模板页代码，并在相应的位置添加了注册页的代码。

![image-20230724205752899.png][17]
![image-20230724205757628.png][18]
![image-20230724205801647.png][19]

如图，上述代码均为base.html模板页的全部代码，当有页面需要继承上述模板时，会先加载模板页，其次可以在{% block %} {% endblock %}等存在可以自定义继承内容处添加内容，例如，base.html页存在\<title\>{% block title %} {% endblock %}\</title\>继承变量为title的修改点，那么regist.html就可以先通过{% extends "base.html" %}继承模板，而后跟上{% block title %} 注 册 {% endblock %}即可让页面的title指为"注册"，这就是Flask默认渲染Jinjia2引擎的特性。

![image-20230724205807018.png][20]

### 3.2.2 邮件验证码

注册用户是需要通过邮件验证码实现的，在上述篇幅中，我们配置了邮件发送的smtp协议用户名以及密码，但是并没有说明如何触发。

![image-20230724205812014.png][21]

在获取邮箱验证码部分，可以看到一个id为email-captcha-btn的button按钮，点击该按钮即可触发邮箱验证码。

![image-20230724205817140.png][22]

在regist.html引入的regist.js代码中，通过jQuery框架，能够很好的实现一个获取验证码并倒计时下次发送时间的效果。这段代码是一个JavaScript脚本，主要用于实现点击按钮后发送请求，获取并发送验证码。

使用jQuery的入口函数 $(function () {})，等待文档加载完毕后执行bindCaptchaBtnClick()函数。

bindCaptchaBtnClick()函数通过$('#email-captcha-btn')寻找id为email-captcha-btn的按钮，并在其上绑定一个click事件。当按钮被点击时，获取邮箱地址并验证是否为空。如果不为空，则通过$.ajax()函数发送一个 POST 请求到 /users/email 的后端服务器端路由，并将邮箱地址作为表单数据发送。

![image-20230724205825287.png][23]

当触发到/user/email的路由后，则需要在后端处理。

如图，上述代码在users蓝图中定义一个/email路由，用于处理发送验证码的 POST 请求。当接收到该请求时，获取表单数据中的邮箱地址，并生成一个随机六位字符串作为验证码。其中，还创建一个Message对象，其中包含发件人、收件人、邮件主题及内容等信息，并调用 mail.send() 函数发送邮件。

![image-20230724205830818.png][24]

![image-20230724205835398.png][25]

其中发送的邮件是通过emialbase.html美化渲染的。

如果发送成功，则将验证码和一些相应的信息存储到 email\_captcha 数据模型中，并将模型提交到数据库。使用query.filter\_by()方法查询 email\_captcha 数据模型是否存在该邮箱地址的记录，如果存在则更新记录中的验证码和时间戳等信息，如果不存在则新建一个数据模型并插入到数据库中，此时存储的内容中包括了当前发送验证码的时间戳以及300秒后即5分钟后过期的时间戳，主要用于验证用户是否在5分钟内注册。最后，返回 JSON 格式数据的响应，包括响应码和消息，即发送成功返回200状态码，失败则为400状态码。

![image-20230724205840316.png][26]

在后端完成上述操作后，在$.ajax()函数的success回调函数中，根据响应结果判断验证码是否发送成功。如果成功，则锁定获取验证码的按钮，设置倒计时并在倒计时结束后重新启用获取验证码按钮。如果不成功，则弹出错误消息。

![image-20230724205845324.png][27]

其中还设置了倒计时的实现方式，调用 setInterval() 函数定时减少倒计时时间，当倒计时时间等于0时，清除计时器并重新绑定获取验证码的点击事件。

![image-20230724205852468.png][28]

validate\_captcha函数是自定义的验证方法，用于验证用户输入的验证码是否正确。首先从表单获取用户输入的验证码和邮箱，然后从数据库中查询该邮箱对应的邮箱验证码信息，并获取当前时间戳。如果当前时间戳小于邮箱验证码的有效时间，则判断用户输入的验证码是否与数据库中存储的验证码相同，如果不相同则抛出 ValidationError 异常，否则验证通过。如果当前时间戳大于邮箱验证码的有效时间，则认为邮箱验证码超时，同样抛出 ValidationError 异常。

validate\_email函数也是自定义的验证方法，用于验证用户输入的邮箱是否已经存在。从表单获取用户输入的邮箱，然后从数据库中查询是否存在该邮箱对应的用户信息。如果存在，则抛出 ValidationError 异常，否则验证通过。

### 3.2.3 用户登录/注销

![image-20230724205857300.png][29]

登录界面的代码比较简单，与regist.html一致，也继承了base.html模板，其中存在一个message参数，用于获取后端返回的一些验证问题。

![image-20230724205901482.png][30]

该函数处理用户登录请求，分为 GET 和 POST 两个请求方式。

当 GET 请求时，直接返回渲染好的 login.html 模板。

![image-20230724205905733.png][31]

如图，当 POST 请求时，首先从表单获取用户输入的邮箱和密码，并实例化 LoginForm 验证器。然后进行表单验证，如果验证通过，则继续进行后续操作；如果验证失败，则返回重新渲染 login.html 模板，并通过 flash() 函数显示密码格式错误的提示信息。

![image-20230724205909201.png][32]

接下来，根据用户输入的邮箱在数据库中查找相应的用户信息，如果不存在则返回重新渲染 login.html 模板，并通过 flash() 函数显示邮箱或密码不匹配的提示信息。如果存在，则使用 check\_password\_hash 函数验证用户输入的密码是否正确。如果验证成功，则将用户的 id 存入 session 中，并重定向到网站首页；如果验证失败，则返回重新渲染 login.html 模板，并通过 flash() 函数显示邮箱或密码不匹配的提示信息。

![image-20230724205913259.png][33]

如图，用户登录成功后会存储Session值。

Session 是指客户端和服务器端之间的一种状态管理机制。在 Web 开发中，客户端和服务器之间一般采用 HTTP 协议进行通信，HTTP 协议是一种无状态的协议，即每个请求和响应之间是独立的，没有维持连接的状态信息。这就会导致无法在不同请求之间共享数据或状态，如保存用户的登录状态等。

为了存储不同请求之间的数据或状态信息，我们可以使用 Session 来进行管理。Session 就是在客户端和服务器端之间建立的一个会话，可以在其中保存一些数据或状态信息，这些信息可以在不同请求之间共享和使用。通常，一个 Session 会对应一个唯一的 Session ID，用于区分不同的会话，Session ID 会以一些形式存储在客户端，例如通过 Cookie 或 URL 参数等。

在 Flask 中，Session 由 Werkzeug 库提供支持，可以非常方便地进行使用。可以使用 session 对象来管理 Session，session 对象提供了一些方法和属性，例如 set、get、pop、getlist 等，用于设置、获取、移除和读取 Session 中的数据或状态信息。同时，也可以通过设置 session 的一些配置参数，例如过期时间、Session ID 的存储方式、签名密钥等，来进行更加灵活的管理。

![image-20230724205918563.png][34]

因此，如果用户需要注销，则只需要清楚当前页面的Session值，并重新加载网页即可。

## 3.3 问答管理

### 3.3.1 限制登录状态

进入问答管理模块，如果用户需要发布问答，则需要登录才能发布相关的信息，如何实现上述功能呢？此时可以自定义一个全局装饰器。

![image-20230724205922509.png][35]

如图，该装饰器实现的是一个登录限制的功能，即只有在用户已经登录的情况下才能访问被装饰的函数。若用户未登录，则被重定向到用户登录页面。

装饰器包含以下步骤：

1. 首先导入 flask.g、 flask.redirect、 flask.url\_for以及 functools.wraps模块。
2. 定义一个名为 login\_required的装饰器，该函数的参数是要被装饰的函数。
3. 用 functools模块中的 wraps函数装饰wrapper函数，保证它能正确地返回装饰的函数名和其他信息。
4. wrapper函数检查global全局变量g中是否有用户对象属性。若存在，则调用原始函数 func，并传入被装饰的函数（通过 \* args和 \*\*kwargs传递)，以及任何其他参数。若不存在，则重定向到用户登录页面，通过 url\_for返回相应路由的 URL，然后通过 Flask中的redirect方法进行重定向。
5. 最后，该装饰器返回了wrapper函数

![image-20230724205927884.png][36]

如图，这将确保在此路由上访问"/answer"路径之前，用户必须登录。

### 3.3.2 发布问答

![image-20230724205931959.png][37]

![image-20230724205936515.png][38]

如图，question\_public.html继承了base.html，并添加了问题标题、问题内容以及发布问答按钮。

![image-20230724205941583.png][39]

如图代码实现了一个可以发布问题的功能，其中使用了Flask的路由和装饰器。

@login\_required作为全局装饰器，对于访问该路由前必须先通过登录认证，否则会跳转至登录页面。

@question.route('/question/public',methods=["GET","POST"])指明了路由，即请求/question/public。根据不同的请求方法（GET或POST），该函数有不同的响应。

当请求为GET方法时，该函数会渲染一个问题发布页面模板并返回渲染后的页面。

![image-20230724205946448.png][40]
当请求为POST方法时，该函数会在QuestionForm表单验证通过的情况下，从request.form中获取表单数据，生成一个新的question\_models对象，并将其加入到数据库中。最后，页面会被重定向到首页。

如果表单验证未通过，将会通过flash()函数闪现出一个提示信息，并重定向到发布页面。

### 3.3.3 问答评论

![image-20230724205950844.png][41]

![image-20230724205955562.png][42]

通过上述代码，当选择某个问题时，自动跳转到该/question/问题id的路径，并且显示问题标题，问题的作者，发布时间，以及发布的内容等，同时支持实时评论。

![image-20230724205959602.png][43]

如图代码实现了一个问题详情页的功能，其中使用了Flask的Get请求的路由。

@question.route('/question/\<int:question\_id\>')指明了路由，即请求/question/{question\_id}，其中\<int:question\_id\>表示该路由后必须传入一个整数类型的参数question\_id。

def question\_detail(question\_id):表示路由处理函数，它需要传入之前指定的question\_id参数。在该函数中，执行了一条针对数据库的查询操作，使用question\_models.query.get(question\_id)将该question\_id对应的问题数据从数据库中取出，并将其存储在一个名为question的变量中。最后，使用Flask提供的render\_template()函数渲染问题详情页面模板，并将取出来的问题数据传入模板中，以便在页面中展示问题的详细信息。

![image-20230724210005953.png][44]

如图代码实现了回答，即评论问题的功能。

@question.route('/answer/\<int:question\_id\>', methods=["post"])指明了路由，即请求/answer/{question\_id}，其中\<int:question\_id\>表示该路由后必须传入一个整数类型的question\_id参数，methods=["post"]表示该路由只能通过POST请求进行访问。

@login\_required作为装饰器，表示对于访问该路由前必须先通过登录认证，否则会跳转至登录页面。

![image-20230724210011240.png][45]

在answer函数中，首先通过AnswerForm(request.form)创建一个登录表单实例。然后通过条件判断，检查用户输入的回答内容是否符合要求。如果表单验证通过，则从表单中获取回答的内容和问题的ID，并将其存储到数据库中。

最后，页面会被重定向到问题详情页面，并将question\_id传入进去。这里需要注意的是，需要使用url\_for()函数生成问题详情页面的URL。如果表单验证未通过，将会通过flash()函数闪现出一个提示信息，并重定向到问题详情页面。同样需要使用url\_for()函数生成问题详情页面的URL，并将question\_id传入进去。

### 3.3.4 搜索功能

![image-20230724210015905.png][46]

在搜索框中输入关键词，则使用Get请求自动跳转到keyword参数等于关键词的页面，此时将会把问题内容与问题标题包含关键词的所有内容全部展现出来。

![image-20230724210020173.png][47]

如图代码实现了一个问题搜索的功能，可以根据问题标题或内容中包含的关键词进行搜索，该路由处理函数限制了用户需要登录才能搜索。

@question.route('/search')指明了路由，即请求/search，该路由处理函数执行搜索操作。

在search函数中，从请求参数中通过request.args.get('keywords')获取关键词，存储在keywords变量中。然后在question\_models中进行查询操作，过滤出标题或内容中包含关键词的问题列表。在这里，用到了or\_()方法来进行or运算，判断标题或内容中是否包含关键词。contains()方法用来判断是否包含关键词。

最后，根据问题创建的时间进行降序排序，并将结果列表传递给index.html模板，用于在页面上展示搜索结果。

### 3.3.5 首页实现

![image-20230724210024427.png][48]

![image-20230724210030671.png][49]

该代码实现了一个首页展示降序的功能。

question = Blueprint('question', \_\_name\_\_, url\_prefix='/')创建了一个蓝图Blueprint，指名了该蓝图名为"question"，url\_prefix="/ "表示该蓝图下的所有路由都要加上"/"作为前缀。

@question.route('/')指明了路由，即请求"/"，该路由处理函数展示了所有问题列表。

在home函数中，通过question\_models.query.order\_by()查询问题数据，并通过db.text('-create\_time')按创建时间降序排序。然后将结果存入questions变量中，并将其传递到模板中渲染。使用render\_template()函数将问题列表渲染到index.html模中，并将渲染后的模板返回到客户端。

## 3.4 数据库更新迁移与管理

在本系统中，使用到了Flask-migrate来快速迁移数据库，Flask\_migrate是Flask的一个扩展，它使用了Alembic这个Python库来实现数据库迁移。其中，Alembic是一个轻量级的数据库迁移工具，它提供了类似于Git的版本控制系统，可以让开发者方便地管理数据库的版本和变更。Flask\_migrate则将Alembic集成到了Flask应用中，提供了一组简单易用的命令来管理数据库迁移。因此，可以说Flask\_migrate和Alembic是密切相关的，Flask\_migrate依赖于Alembic来实现数据库迁移功能。

下面简单介绍一下如何使用Flask\_migrate迁移数据库。

### 3.4.1 安装依赖环境

由于Flask\_migrate与Alembic是Python语言的第三方库，因此可以使用pip包管理工具来直接安装。

![image-20230724210036059.png][50]

在终端环境中激活项目的虚拟环境Flask-Answer，输入pip install flask-migrate alembic命令，即可安装最新版本的Flask\_migrate与Alembic。

![image-20230724210044449.png][51]

如图，在Installing collected packages后的第三库都是被安装成功的，可以发现不仅仅安装了Flask-migrate和Alembic，这是因为如果这两个库依赖的环境不存在，也会被一同安装，在Python中，许多库是相互依赖而存在的，例如：Flask-migrate是Flask库的扩展，如果没有Flask框架就无法正常使用，那么此时安装了Flask-migrate则会自动将Flask安装。

### 3.4.2 SQLAlchemy配置

在Flask应用中，可以在配置文件中配置数据库的连接参数。

常见的数据库有MySQL、PostgreSQL、SQLite等，配置方式可以参见各自的文档。本项目以MySQL为例，可以在Flask应用的配置文件中添加如下代码：

![image-20230724210049673.png][52]

如图，在配置文件中，新建了MYSQLCONFIG的字典，并通过Key键对Value值的方式，存储了MYSQL的IP地址、MYSQL的默认端口、MYSQL的登录用户名与密码以及MYSQL连接后默认打开的数据库名称。

通过DB\_URL设置数据库的链接信息，并使用\*\*MYSQLCONFIG对其解包，使得每个参数都对应相应的值，并赋值给SQLAlchemy\_DATABASE\_URI，其中，SQLAlchemy\_DATABASE\_URI指定数据库连接的URI，即指定迁移的数据库。

### 3.4.3 初始化Flask\_migrate

在Flask应用中，如果需要使用Flask\_migrate扩展，则必须对其初始化，因此在app应用实例中需要添加如下代码：

![image-20230724210054835.png][53]

如图，通过上述代码完成了导入Flask\_migrate与SQLAlchemy等相应模块，并对数据完成SQLAlchemy实例化，与Flask\_migrate进行绑定，而后初始化一个Flask应用，并与Flask\_migrate和SQLAlchemy初始化。即绑定数据，完成应用与数据的ORM映射，数据迁移扩展，同时应用项目相互绑定并在应用中注册初始化。

![image-20230724210059695.png][54]

在本项目中，为了项目的可持久与可维护性，创建过项目扩展文件project\_extension.py，而db即SQLAlchemy实例是从中导入的，其他的代码与上述的基本思路大致上没有差别，由此完成了Flask-migrate等应用插件的初始化。

### 3.4.4 创建与迁移

![image-20230724210103934.png][55]

flask db init是使用Flask-Migrate进行数据库迁移时的一个命令，其作用是初始化迁移仓库。在使用Flask-Migrate进行数据库迁移时，需要先创建一个迁移仓库来存储版本信息和迁移脚本。通过执行flask db init命令，会自动在项目目录下创建一个名为migrations的目录，用于保存迁移仓库。migrations目录中将会生成若干文件和目录，包括一个versions目录用于存储所有的迁移脚本，一个migrate.ini文件用于配置Alembic，以及一个script.py.mako文件用于在版本之间生成迁移脚本的模板文件。

需要注意的是，flask db init只需要执行一次，用于初始化迁移仓库。在之后的迭代中，如果数据模型存在更新，则只需要执行flask db migrate来生成新的迁移脚本，并使用flask db upgrade来应用迁移脚本即可。

![image-20230724210108307.png][56]

使用Navicat查看数据库信息，当前数据库并不存在任何数据表。

![image-20230724210113088.png][57]

如图，在使用flask db init 初始化仓库后，执行flask db migrate命令，将自动生成迁移的脚本，当添加了-m参数后，可以跟上双引号的字符串，用于注释本次迁移脚本的说明，这样就会生成一个"随机版本号\_迁移说明.py"的迁移脚本文件，图中的df231aaec8de就是随机生成的版本号。

![image-20230724210117433.png][58]

可以看到，通过flask db migrate 生成的迁移脚本中，包含了该项目所使用到的所有数据模型，值得注意的是flask db migrate命令生成的迁移脚本中，包含两个函数：upgrade()和downgrade()。其中，upgrade()函数用于将数据库升级到新版本，而downgrade()函数则用于将数据库降级回旧版本。

当需要回退到旧版本时，可以使用flask db downgrade命令应用downgrade()函数中的逻辑。在回退之前，需要确认数据库中的数据和结构是否是在回退前的状态，否则可能会造成数据的丢失或损坏。

例如，在生成迁移脚本时，Alembic会自动为每个升级操作创建一个对应的降级操作。如果在数据库升级后发现某个操作造成了问题，可以使用flask db downgrade进行回退。该命令会执行downgrade()函数中相应版本的操作，将数据库回退到指定的上一个版本。

需要注意的是，虽然downgrade()函数可以将数据库回退到旧版本，但是不能完全保证数据的一致性。因此，在使用flask db downgrade命令回退时，需要在回退前备份数据库，以便后续恢复。

![image-20230724210123297.png][59]

其次，执行flask db migrate命令后，原本没有任何表的数据库会自动创建一个alembic\_version的数据表，其中只包含了一个数据类型为varchar(32)的version\_num列名，它用于存储数据库迁移的版本号，不过，此时version\_num的值为空值，这是因为数据还未正式迁移。

![image-20230724210127853.png][60]

flask db upgrade命令是Flask-migrate中用于应用迁移脚本的命令，其作用是将数据库从当前版本升级到新版本。

在使用Flask-migrate进行数据库迁移时，需要通过flask db migrate命令生成迁移脚本，然后通过flask db upgrade命令应用迁移脚本。当执行flask db upgrade命令时，将应用由flask db migrate生成的所有尚未应用的迁移脚本，并将数据库迁移到最新的版本。

例如，假设我们当前的数据库版本为1，而使用了flask db migrate命令生成了版本号为2的2\_add\_user\_table.py迁移脚本，用于向数据库中添加一个名为user的表。那么，使用flask db upgrade命令即可将数据库升级到新版本。

本项目中则是将df231aaec8de版本脚本执行，并更新数据库，完成迁移。

![image-20230724210131785.png][61]

如图，执行了flask db upgrade后alembic\_version的version\_num值从空值变成了df231aaec8de，并且原本只有一个数据表的数据库也添加创建了本项目中所需要使用到的若干数据表。

![image-20230724210135943.png][62]

此时数据库已经完成了更新迁移，并且成功创建了主键与外键的表关系。

综上所述，使用Flask-Migrate完成数据库的迁移需要结合安装依赖环境，配置SQLAlchemy的URL指向，而后使用flask db init初始化环境、使用flask db migrate生产迁移脚本，使用flask db upgrade完成数据库的更新与迁移。

需要注意的是，在进行迁移操作前，请务必先库备份重要数据，避免迁移过程中数据丢失产生的不必要损失。

# 参考文献

1. 余晓帆,朱丽青.基于Flask框架的社交网站数据爬取及分析[J].微型电脑应用,2022.
2. 田胜男. 基于Flask的智能小区物业管理系统设计与实现[D].华东师范大学,2022.
3. 张明.基于Flask+Webhook技术的观影问卷调查数据收集方案设计[J].现代电影技术,2022.
4. 王方雄,刘欣钰,王俊夫等.基于Flask的AIS大数据地理信息系统研究与开发[J].软件,2022.
5. 来思琪,孔华锋.基于Flask框架的新闻聚合系统设计与实现[J].电脑编程技巧与维护,2022.
6. 陈嘉发,黄宇靖.Flask框架在数据可视化的应用[J].福建电脑,2022.
7. 奋斗的源.Flask之models（一）:ORM、SQLAlchemy、flask-migrate [EB/OL]. https://blog.csdn.net/yuanfate/article/details/105499342,2020.
8. keinYe.Python 数据库迁移工具 Alembic [EB/OL].https://zhuanlan.zhihu.com/p/90106173,2019.
9. 夏晓旭.flask 使用Flask-Migrate迁移数据库（创建迁移环境、生成迁移脚本、更新数据库）.https://www.cnblogs.com/xiaxiaoxu/p/10652054.html,2019.
10. [微雨燕凝霜寒](https://blog.csdn.net/xu1227233860).使用Navicat生成ER关系图并导出[EB/OL].https://blog.csdn.net/xu1227233860/article/details/78278393,2017.


  [1]: https://blog.xcup.top/usr/uploads/2023/07/4230181379.png
  [2]: https://blog.xcup.top/usr/uploads/2023/07/645995654.png
  [3]: https://blog.xcup.top/usr/uploads/2023/07/4028849485.png
  [4]: https://blog.xcup.top/usr/uploads/2023/07/2479908003.png
  [5]: https://blog.xcup.top/usr/uploads/2023/07/2254362542.png
  [6]: https://blog.xcup.top/usr/uploads/2023/07/1519060757.png
  [7]: https://blog.xcup.top/usr/uploads/2023/07/3245342133.png
  [8]: https://blog.xcup.top/usr/uploads/2023/07/3735065033.png
  [9]: https://blog.xcup.top/usr/uploads/2023/07/4288513146.png
  [10]: https://blog.xcup.top/usr/uploads/2023/07/3229590044.png
  [11]: https://blog.xcup.top/usr/uploads/2023/07/148541878.png
  [12]: https://blog.xcup.top/usr/uploads/2023/07/3223639529.png
  [13]: https://blog.xcup.top/usr/uploads/2023/07/2887957971.png
  [14]: https://blog.xcup.top/usr/uploads/2023/07/2887957971.png
  [15]: https://blog.xcup.top/usr/uploads/2023/07/1755718437.png
  [16]: https://blog.xcup.top/usr/uploads/2023/07/1993960545.png
  [17]: https://blog.xcup.top/usr/uploads/2023/07/2997145261.png
  [18]: https://blog.xcup.top/usr/uploads/2023/07/1357157518.png
  [19]: https://blog.xcup.top/usr/uploads/2023/07/4273370321.png
  [20]: https://blog.xcup.top/usr/uploads/2023/07/3147597987.png
  [21]: https://blog.xcup.top/usr/uploads/2023/07/1096543473.png
  [22]: https://blog.xcup.top/usr/uploads/2023/07/1497146281.png
  [23]: https://blog.xcup.top/usr/uploads/2023/07/1466130922.png
  [24]: https://blog.xcup.top/usr/uploads/2023/07/2905327320.png
  [25]: https://blog.xcup.top/usr/uploads/2023/07/4115087100.png
  [26]: https://blog.xcup.top/usr/uploads/2023/07/4114274805.png
  [27]: https://blog.xcup.top/usr/uploads/2023/07/1353947747.png
  [28]: https://blog.xcup.top/usr/uploads/2023/07/1915353629.png
  [29]: https://blog.xcup.top/usr/uploads/2023/07/2006669293.png
  [30]: https://blog.xcup.top/usr/uploads/2023/07/3398109901.png
  [31]: https://blog.xcup.top/usr/uploads/2023/07/4170068089.png
  [32]: https://blog.xcup.top/usr/uploads/2023/07/2591045393.png
  [33]: https://blog.xcup.top/usr/uploads/2023/07/37059125.png
  [34]: https://blog.xcup.top/usr/uploads/2023/07/4262181341.png
  [35]: https://blog.xcup.top/usr/uploads/2023/07/3401176998.png
  [36]: https://blog.xcup.top/usr/uploads/2023/07/2390225629.png
  [37]: https://blog.xcup.top/usr/uploads/2023/07/88020293.png
  [38]: https://blog.xcup.top/usr/uploads/2023/07/309427086.png
  [39]: https://blog.xcup.top/usr/uploads/2023/07/2849017569.png
  [40]: https://blog.xcup.top/usr/uploads/2023/07/2229679567.png
  [41]: https://blog.xcup.top/usr/uploads/2023/07/978485588.png
  [42]: https://blog.xcup.top/usr/uploads/2023/07/3428382077.png
  [43]: https://blog.xcup.top/usr/uploads/2023/07/2635054736.png
  [44]: https://blog.xcup.top/usr/uploads/2023/07/1554089902.png
  [45]: https://blog.xcup.top/usr/uploads/2023/07/4167756750.png
  [46]: https://blog.xcup.top/usr/uploads/2023/07/941523178.png
  [47]: https://blog.xcup.top/usr/uploads/2023/07/854239581.png
  [48]: https://blog.xcup.top/usr/uploads/2023/07/2630131782.png
  [49]: https://blog.xcup.top/usr/uploads/2023/07/2237165678.png
  [50]: https://blog.xcup.top/usr/uploads/2023/07/2339239730.png
  [51]: https://blog.xcup.top/usr/uploads/2023/07/3460505895.png
  [52]: https://blog.xcup.top/usr/uploads/2023/07/3573101966.png
  [53]: https://blog.xcup.top/usr/uploads/2023/07/327954429.png
  [54]: https://blog.xcup.top/usr/uploads/2023/07/2314885629.png
  [55]: https://blog.xcup.top/usr/uploads/2023/07/1474584679.png
  [56]: https://blog.xcup.top/usr/uploads/2023/07/2771885862.png
  [57]: https://blog.xcup.top/usr/uploads/2023/07/1108104938.png
  [58]: https://blog.xcup.top/usr/uploads/2023/07/539034840.png
  [59]: https://blog.xcup.top/usr/uploads/2023/07/3271368276.png
  [60]: https://blog.xcup.top/usr/uploads/2023/07/1158443031.png
  [61]: https://blog.xcup.top/usr/uploads/2023/07/1391546969.png
  [62]: https://blog.xcup.top/usr/uploads/2023/07/1251110892.png
