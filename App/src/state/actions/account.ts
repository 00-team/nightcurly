import { Dispatch } from 'redux'
import { Action } from '../action-types/account'
import { AccountTypes } from '../models/Account'

// axios
import axios from 'axios'

// cookies
import { get as GetCookies } from 'js-cookie'

const BASE_URL = '/api/account/'

const HandleError = (error: unknown): string => {
    if (
        axios.isAxiosError(error) &&
        error.response &&
        error.response.data.error
    ) {
        ReactAlert.error(error.response.data.error)
        return error.response.data.error
    }

    return 'There Was An error changing your wallet'
}
type D = (d: Dispatch<Action>) => Promise<void>
type GA = () => D
const GetAccount: GA = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'get/')

        dispatch({ type: AccountTypes.SET_ACCOUNT, payload: data })
    } catch (error) {
        HandleError(error)
    }
}

type UA = (wallet: string) => (d: Dispatch<Action>) => Promise<[string, string]>
const UpdateAccount: UA = wallet => async dispatch => {
    try {
        const csrftoken = GetCookies('csrftoken')
        if (!csrftoken) {
            location.reload()
            return ['error', 'Error! pls reload']
        }

        const config = {
            headers: { 'X-CSRFToken': csrftoken },
        }

        const UpdateData = {
            wallet: wallet,
        }

        const { data } = await axios.post(
            BASE_URL + 'update/',
            UpdateData,
            config
        )

        if (data.ok) {
            dispatch({ type: AccountTypes.SET_WALLET, payload: data.wallet })
            ReactAlert.success(data.ok)
            return ['success', data.ok]
        }
    } catch (error) {
        return ['error', HandleError(error)]
    }

    return ['error', 'An Unknown Error Happend.']
}
export { GetAccount, UpdateAccount }

type DT = () => (d: Dispatch<any>) => Promise<void>
const DisconnectTwitter: DT = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'disconnect_twitter/')

        dispatch(GetAccount())

        if (data.ok) ReactAlert.success(data.ok)
    } catch (error) {
        HandleError(error)
    }
}
export { DisconnectTwitter }

type UGT = () => (d: Dispatch<Action>) => Promise<void>
const UpdateGeneralInfo: UGT = () => async dispatch => {
    try {
        const { data } = await axios.get(BASE_URL + 'general_info/')

        dispatch({ type: AccountTypes.SET_GENERAL_INFO, payload: data })
    } catch (error) {
        HandleError(error)
    }
}
export { UpdateGeneralInfo }

enum MessageLevel {
    INFO = 20,
    SUCCESS = 25,
    WARNING = 30,
    ERROR = 40,
}
interface Message {
    message: string
    level: MessageLevel
    tags: string
}

const GetMessages = async () => {
    try {
        const { data } = await axios.get(BASE_URL + 'messages/')
        if (data.messages && typeof data.messages == 'object') {
            data.messages.map(({ message, level }: Message) => {
                switch (level) {
                    case MessageLevel.INFO:
                        ReactAlert.info(message)
                        break
                    case MessageLevel.SUCCESS:
                        ReactAlert.success(message)
                        break
                    default:
                        ReactAlert.error(message)
                        break
                }
            })
        }
    } catch (error) {
        HandleError(error)
    }
}

export { GetMessages }
