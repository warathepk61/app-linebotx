def flex_timetable():
      flex = '''{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": %s,
            "weight": "bold",
            "color": "#FF9933",
            "size": "xl"
          },
          {
            "type": "text",
            "text": %s,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "Class schedule "%s,
            "size": "sm",
            "color": "#aaaaaa"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": %s,
                "flex": 1,
                "weight": "bold",
                "size": "lg",
                "color": "#FAD000"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": %s,
                    "size": "sm",
                    "weight": "bold",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": %s,
                    "weight": "bold",
                    "size": "sm"
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "room : "%s,
                    "size": "sm",
                    "contents": [
                      {
                        "type": "span",
                        "text": "sec: "%s,
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "room : "%s,
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "time : "%s,
                        "color": "#aaaaaa"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001202",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Computer Technology -3",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2203 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 13:00 - 15:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001203",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C)  Academic Analysis in Computer Technology -1 ",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2  ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2204 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 10:00 - 12:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001205",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Biology - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:3 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2208 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 15:00 - 17:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001206",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C) Internet Programming - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:1 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2201 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 17:00 - 19:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "61314601",
            "weight": "bold",
            "color": "#FF9933",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "Mr.Sawaddee Taweesuk",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "Class schedule 2/2564",
            "size": "sm",
            "color": "#aaaaaa"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Tuesday",
                "flex": 1,
                "weight": "bold",
                "size": "lg",
                "color": "#ff99cc"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "001201",
                    "size": "sm",
                    "weight": "bold",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "(C) Communicative English for Academic Analysis in Computer Technology -1 ",
                    "weight": "bold",
                    "size": "sm"
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "room :  QS2201 ",
                    "size": "sm",
                    "contents": [
                      {
                        "type": "span",
                        "text": "sec:1 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "room : QS2201 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "time : 08:00 - 10:00",
                        "color": "#aaaaaa"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001202",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Computer Technology -3",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2203 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 13:00 - 15:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001203",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C)  Academic Analysis in Computer Technology -1 ",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2204 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 10:00 - 12:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001205",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Biology - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:3 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2208 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 15:00 - 17:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001206",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C) Internet Programming - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:1 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2201 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 17:00 - 19:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "61314601",
            "weight": "bold",
            "color": "#FF9933",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "Mr.Sawaddee Taweesuk",
            "flex": 1,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "Class schedule 2/2564",
            "flex": 1,
            "size": "sm",
            "color": "#aaaaaa"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Wednesday",
                "flex": 1,
                "weight": "bold",
                "size": "lg",
                "color": "#299438"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "001201",
                    "size": "sm",
                    "weight": "bold",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "(C) Communicative English for Academic Analysis in Computer Technology -1 ",
                    "weight": "bold",
                    "size": "sm"
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "room :  QS2201 ",
                    "size": "sm",
                    "contents": [
                      {
                        "type": "span",
                        "text": "sec:1 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "room : QS2201 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "time : 08:00 - 10:00",
                        "color": "#aaaaaa"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001202",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Computer Technology -3",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2203 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 13:00 - 15:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001203",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C)  Academic Analysis in Computer Technology -1 ",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2204 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 10:00 - 12:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001205",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Biology - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2208 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 15:00 - 17:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001206",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C) Internet Programming - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2201 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 17:00 - 19:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "61314601",
            "weight": "bold",
            "color": "#FF9933",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "Mr.Sawaddee Taweesuk",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "Class schedule 2/2564",
            "size": "sm",
            "color": "#aaaaaa"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "weight": "bold",
                "size": "lg",
                "color": "#FF9933",
                "text": "Thursday"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "001201",
                    "size": "sm",
                    "weight": "bold",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "(C) Communicative English for Academic Analysis in Computer Technology -1 ",
                    "weight": "bold",
                    "size": "sm"
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "room :  QS2201 ",
                    "size": "sm",
                    "contents": [
                      {
                        "type": "span",
                        "text": "sec:1 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "room : QS2201 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "time : 08:00 - 10:00",
                        "color": "#aaaaaa"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001202",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Computer Technology -3",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2203 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 13:00 - 15:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001203",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C)  Academic Analysis in Computer Technology -1 ",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2204 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 10:00 - 12:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001205",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Biology - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2208 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 15:00 - 17:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001206",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C) Internet Programming - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2201 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 17:00 - 19:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "61314601",
            "weight": "bold",
            "color": "#FF9933",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "Mr.Sawaddee Taweesuk",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "Class schedule 2/2564",
            "size": "sm",
            "color": "#aaaaaa"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Friday",
                "flex": 1,
                "weight": "bold",
                "size": "lg",
                "color": "#00a5e3"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "001201",
                    "size": "sm",
                    "weight": "bold",
                    "flex": 0
                  },
                  {
                    "type": "text",
                    "text": "(C) Communicative English for Academic Analysis in Computer Technology -1 ",
                    "weight": "bold",
                    "size": "sm"
                  }
                ],
                "spacing": "xs"
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "room :  QS2201 ",
                    "size": "sm",
                    "contents": [
                      {
                        "type": "span",
                        "text": "sec:1 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "room : QS2201 ",
                        "color": "#aaaaaa"
                      },
                      {
                        "type": "span",
                        "text": "time : 08:00 - 10:00",
                        "color": "#aaaaaa"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001202",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Computer Technology -3",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2203 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 13:00 - 15:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001203",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C)  Academic Analysis in Computer Technology -1 ",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2204 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 10:00 - 12:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001205",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(L) Biology - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2208 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 15:00 - 17:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "001206",
                        "size": "sm",
                        "weight": "bold",
                        "flex": 0
                      },
                      {
                        "type": "text",
                        "text": "(C) Internet Programming - 1",
                        "weight": "bold",
                        "size": "sm"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "room :  QS2201 ",
                        "size": "sm",
                        "contents": [
                          {
                            "type": "span",
                            "text": "sec:2 ",
                            "color": "#AAAAAA"
                          },
                          {
                            "type": "span",
                            "text": "room : QS2201 ",
                            "color": "#aaaaaa"
                          },
                          {
                            "type": "span",
                            "text": "time : 17:00 - 19:00",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}'''
      return flex