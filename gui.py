{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "computational-liabilities",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter\n",
    "from tkinter import *\n",
    "\n",
    "\n",
    "def send():\n",
    "    msg = EntryBox.get(\"1.0\",'end-1c').strip()\n",
    "    EntryBox.delete(\"0.0\",END)\n",
    "\n",
    "    if msg != '':\n",
    "        ChatLog.config(state=NORMAL)\n",
    "        ChatLog.insert(END, \"You: \" + msg + '\\n\\n')\n",
    "        ChatLog.config(foreground=\"#442265\", font=(\"Arial\", 12 ))\n",
    "\n",
    "        res = chatbot_response(msg)\n",
    "        ChatLog.insert(END, \"StudentBot: \" + res + '\\n\\n')\n",
    "\n",
    "        ChatLog.config(state=DISABLED)\n",
    "        ChatLog.yview(END)\n",
    "\n",
    "\n",
    "base = Tk()\n",
    "base.title(\"StudentBot of the University of St.Gallen\")\n",
    "base.config(bg=\"dark green\")\n",
    "base.geometry(\"400x500\")\n",
    "base.resizable(width=False, height=False)\n",
    "icon_photo = PhotoImage(file = \"1000px-Universitaet-st-gallen.svg1.png\")\n",
    "base.iconphoto(False, icon_photo)\n",
    "\n",
    "#Create a background using an image\n",
    "send_button = PhotoImage(file = \"send_image.png\")\n",
    "img_bg = Label(image=send_button)\n",
    "img_bg.pack(pady=30)\n",
    "\n",
    "#Create Chat window\n",
    "ChatLog = Text(base, bd=0, bg=\"white\", height=\"8\", width=\"50\", font=\"Arial\",)\n",
    "\n",
    "ChatLog.config(state=DISABLED)\n",
    "\n",
    "#Bind scrollbar to Chat window\n",
    "scrollbar = Scrollbar(base, command=ChatLog.yview, cursor=\"\")\n",
    "ChatLog['yscrollcommand'] = scrollbar.set\n",
    "\n",
    "#Create Button to send message\n",
    "SendButton = Button(base, font=(\"Arial\",12,'bold'), text=\"Send\", width=\"12\", height=5,\n",
    "                    bd=0, bg=\"#32de97\", activebackground=\"#3c9d9b\",fg='#ffffff',\n",
    "                    command= send )\n",
    "\n",
    "#Create the box to enter message\n",
    "EntryBox = Text(base, bd=0, bg=\"white\",width=\"29\", height=\"5\", font=\"Arial\")\n",
    "#EntryBox.bind(\"<Return>\", send)\n",
    "\n",
    "\n",
    "#Place all components on the screen\n",
    "scrollbar.place(x=376,y=6, height=386)\n",
    "ChatLog.place(x=6,y=6, height=386, width=370)\n",
    "EntryBox.place(x=128, y=400, height=90, width=265)\n",
    "SendButton.place(x=6, y=400, height=90)\n",
    "\n",
    "base.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "infrared-preference",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "arctic-allen",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
